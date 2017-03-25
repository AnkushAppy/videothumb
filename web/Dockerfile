FROM ubuntu:latest
MAINTAINER Ankuah Patel "ankush14.dev@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN apt-get install -y cython libavcodec-dev libavformat-dev libswscale-dev
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["run.py"]
