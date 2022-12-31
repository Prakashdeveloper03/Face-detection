from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from fastapi.templating import Jinja2Templates
from camera import VideoCamera

app = FastAPI()
templates = Jinja2Templates(directory="templates")


def generate(camera):
    while True:
        frame = camera.get_frame()
        yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n\r\n")


@app.get("/")
def video_feed():
    return StreamingResponse(
        generate(VideoCamera()), media_type="multipart/x-mixed-replace;boundary=frame"
    )


@app.get("/camera")
async def read_item(request: Request):
    return templates.TemplateResponse("camera.html", {"request": request})
