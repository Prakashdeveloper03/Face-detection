# Face Detection
![made-with-python](https://img.shields.io/badge/Made%20with-Python-0078D4.svg)
![html5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![css3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![opencv](https://img.shields.io/badge/OpenCV-27338e?logo=OpenCV&logoColor=white)
![fastapi](https://img.shields.io/badge/Fastapi-109989?logo=FASTAPI&logoColor=white)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

I built a simple face recognition using opencv find all rectangular areas that contains faces in live stream video.

## Installation
Open Anaconda prompt and create new environment
```
conda create -n your_env_name python = (any_version_number > 3.10.4)
```
Then Activate the newly created environment
```
conda activate your_env_name
```
Clone the repository using `git`
```
git clone https://github.com/Prakashdeveloper03/Face-detection.git
```
Change to the cloned directory
```
cd <directory_name>
```
To install all requirement packages for the app
```
pip install -r requirements.txt
```
Then, Run the app
```
uvicorn main:app --reload
```