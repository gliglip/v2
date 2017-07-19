FROM python:3.6.1
LABEL maintainer="caulagi@gmail.com"

COPY requirements/common.txt /tmp/common.txt
COPY requirements/prod.txt /tmp/prod.txt

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
            libproj-dev=4.8.0-5 \
            gdal-bin=1.10.1+dfsg-8+b3 \
    && rm -rf /var/lib/apt/lists/*


RUN pip3 install -r /tmp/prod.txt

COPY . /code
WORKDIR /code

ENV PG_HOST docker
ENV DJANGO_SETTINGS_MODULE settings.prod

CMD ["python", "app/manage.py", "runserver", "0.0.0.0:8000"]
