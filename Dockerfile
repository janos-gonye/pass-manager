FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /www/pass_manager
RUN pip install --upgrade pip

# psycopg2-binary needs these
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
ADD requirements.txt ./
RUN pip install -r requirements.txt

ADD . ./
