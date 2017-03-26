# videothumb

Aim: To upload Upload a Video file (.mp4, max size of 10 MB) and Generate a thumbnail image of that video file

Other Goals: Use REST APIs, Docker, Documentation

Tech Stack: Python(Flask)

- Usage:
```buildoutcfg

git clone https://github.com/AnkushAppy/videothumb.git
```

1) running using virtualenv:

```buildoutcfg
cd videothumb
cd web
virtualenv venv
pip install -r requirements.txt
python run.py

```

open browser and visit **localhost:5000**

2) running using docker:
```buildoutcfg
cd videothumb
cd web
sudo docker build -t image_name .
sudo docker run -p 5000:5000 --name container_name -d -it image_name
```
open browser and visit **localhost:5000**
 
3) running using docker-compose
```buildoutcfg
cd videothumb
sudo docker-compose build .
sudo docker-compose up
```

- API 




 
