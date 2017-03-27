# videothumb

Aim: To upload Upload a Video file (.mp4 .mpg, max size of 10 MB) and Generate a thumbnail image of that video file

Other Goals: Use REST APIs, Docker, Documentation

Tech Stack: Python(Flask)

Site is Live: http://52.23.163.70/
- Usage:
```buildoutcfg

git clone https://github.com/AnkushAppy/videothumb.git
```

1) running using virtualenv:

```buildoutcfg
cd videothumb
cd web
virtualenv venv
. venv/bin/activate
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

Request: POST /upload
```json
cURL: curl -X POST -H "Cache-Control: no-cache"  \
      -H "Content-Type: multipart/form-data" \
      -F "file=@test-mpeg.mpg" "http://localhost:5000/upload"

Response:
for success:
{
  "filename": "test-mpeg.mpg",
  "status": "Uploaded"
}

for failure:
{
  "status": "This file extesion not allowed."
}

or 

{
  "status": "File size more then 10Mb."
}

```

Request: GET /files
```json
cURL: curl -X GET -H "Cache-Control: no-cache"  "http://localhost:5000/files"
Response:
{
  "files": [
    "test-mpeg.jpeg",
    "centaur_2.jpeg"
  ],
  "status": "OK"
}

```




 
