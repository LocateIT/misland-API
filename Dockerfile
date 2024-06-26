FROM python:3.9-alpine

USER root

RUN apk update && apk upgrade && \
    apk add --no-cache --update bash git openssl-dev build-base alpine-sdk \
    libffi-dev postgresql-dev gcc python3-dev musl-dev

RUN apk add --no-cache --update py3-pip
RUN pip install --upgrade pip

RUN pip install virtualenv gunicorn gevent

RUN mkdir -p /opt/misland-api
RUN cd /opt/misland-api && virtualenv venv && source venv/bin/activate
COPY requirements.txt /opt/misland-api/requirements.txt
RUN cd /opt/misland-api && pip install -r requirements.txt

COPY entrypoint.sh /opt/misland-api/entrypoint.sh
COPY main.py /opt/misland-api/main.py
COPY gunicorn.py /opt/misland-api/gunicorn.py

# Copy the application folder inside the container
WORKDIR /opt/misland-api

COPY ./misland_api /opt/misland-api/misland_api
COPY ./migrations /opt/misland-api/migrations
COPY ./tests /opt/misland-api/tests

# Tell Docker we are going to use these ports
EXPOSE 3000

# Launch script
ENTRYPOINT ["sh", "./entrypoint.sh"]
