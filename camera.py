import cv2

face_cascade = cv2.CascadeClassifier(
    f"{cv2.data.haarcascades}haarcascade_frontalface_alt2.xml"
)


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        _, image = self.video.read()
        image = cv2.flip(image, 1)
        image = cv2.resize(image, None, fx=0.6, fy=0.6, interpolation=cv2.INTER_AREA)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face_rects = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in face_rects:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            break
        _, jpeg = cv2.imencode(".jpg", image)
        return jpeg.tobytes()
