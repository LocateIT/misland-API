FROM python:3.9-alpine

ENV NAME misland-api
ENV USER misland-api

RUN apk update && apk upgrade && \
   apk add --no-cache --update bash git openssl-dev build-base alpine-sdk \
   libffi-dev postgresql-dev gcc python3-dev musl-dev

RUN addgroup $USER && adduser -s /bin/bash -D -G $USER $USER

RUN apk add --no-cache --update py3-pip
RUN pip install --upgrade pip

RUN pip install virtualenv gunicorn gevent

RUN mkdir -p /opt/$NAME
RUN cd /opt/$NAME && virtualenv venv && source venv/bin/activate
COPY requirements.txt /opt/$NAME/requirements.txt
RUN cd /opt/$NAME && pip install -r requirements.txt

COPY entrypoint.sh /opt/$NAME/entrypoint.sh
COPY main.py /opt/$NAME/main.py
COPY gunicorn.py /opt/$NAME/gunicorn.py
# COPY config.json /root/.docker/config.json

# Copy the application folder inside the container
WORKDIR /opt/$NAME

COPY ./misland_api /opt/$NAME/misland_api
COPY ./migrations /opt/$NAME/migrations
COPY ./tests /opt/$NAME/tests
RUN chown -R $USER:$USER /opt/$NAME
RUN chown -R  $USER:$USER /var/log/
RUN chown -R  $USER:$USER /var/run/
# Tell Docker we are going to use this ports
EXPOSE 3000
USER root
# USER $USER

# install docker-compose wait
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.12.0/wait /wait
RUN chmod +x /wait

# Launch script
ENTRYPOINT ["sh","./entrypoint.sh"]
