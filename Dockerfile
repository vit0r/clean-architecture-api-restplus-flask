FROM python:3.7.5-slim-stretch

ARG USER_NAME=userapp
ARG USER_HOME=/home/${USER_NAME}

RUN useradd -ms /bin/bash -d ${USER_HOME} ${USER_NAME} \
    && apt update \
    && apt upgrade -y \
    && apt install nginx supervisor -y \
    && pip install --no-cache pipenv \
    && apt-cache clean

WORKDIR ${USER_HOME}

ADD ./Pipfile ./Pipfile
RUN pipenv lock --pre && pipenv sync

ADD ./apis ./apis
ADD ./app ./app
ADD ./core ./core
ADD ./flask-db.sh ./flask-db.sh

EXPOSE 5000

ENTRYPOINT [ "gunicorn", "app:app", "-b", "localhost:5000 &" ]