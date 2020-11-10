FROM python:3.7-alpine3.12
LABEL "Auther"="Fazlul Haque"

ENV PYTHONUNBUFFERED 1

COPY ./requirments.txt /requirments.txt
RUN pip install -r /requirments.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D faz13
USER faz13