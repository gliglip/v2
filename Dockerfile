FROM python:3.6.1
LABEL maintainer="caulagi@gmail.com"

COPY requirements/common.txt requirements/prod.txt /tmp/

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
            libproj-dev=4.8.0-5 \
            gdal-bin=1.10.1+dfsg-8+b3 \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install -r /tmp/prod.txt

COPY . /code
WORKDIR /code/app

ENV PG_HOST docker
ENV DJANGO_SETTINGS_MODULE settings.prod

CMD ["uwsgi", "--ini", "uwsgi.ini"]
