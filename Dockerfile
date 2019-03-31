FROM python:3.6

ENV PYTHONBUFFERED 1

WORKDIR /profiles_project

COPY . /profiles_project

RUN pip install -r requirements.txt