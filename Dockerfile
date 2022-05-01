FROM python:3.8

WORKDIR /usr/src/app

COPY ./Pipfile /usr/src/app
COPY ./Pipfile.lock /usr/src/app

RUN pip install pipenv

RUN pipenv install --system

COPY . /usr/src/app