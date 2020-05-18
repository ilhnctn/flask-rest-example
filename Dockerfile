FROM python:3.8.3
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY . /code/.

RUN pip install -r requirements/development.txt