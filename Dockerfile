FROM python:3.7-alpine3.12
LABEL "Auther"="Fazlul Haque"

ENV PYTHONUNBUFFERED 1

COPY ./requirments.txt /requirments.txt
RUN apk add --update --no-cache mariadb-client mariadb-connector-c
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev mariadb-dev
RUN pip install -r /requirments.txt
RUN apk del .tmp-build-deps
RUN mkdir /app
WORKDIR /app
COPY ./app /app
RUN adduser -D faz13
USER faz13