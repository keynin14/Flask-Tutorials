from mimetypes import init
from multiprocessing.pool import RUN


FROM python:3.13-slim-buster

WORKDIR /flask-app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . . 

WORKDIR /flask-app/Deployment_and_Docker

RUN flask db init
RUN flask db migrate
RUN flask db upgrade

WORKDIR /flask-app

CMD ["python3", "run.py"]