FROM python:3.6.1

COPY requirements/common.txt /tmp/common.txt
COPY requirements/prod.txt /tmp/prod.txt

RUN apt-get update \
        && apt-get install -y --no-install-recommends \
                binutils \
                libproj-dev \
                gdal-bin \
        && rm -rf /var/lib/apt/lists/*

RUN pip3 install -r /tmp/prod.txt

ADD . /code
WORKDIR /code

ENV DJANGO_SETTINGS_MODULE settings.prod

CMD ["python", "app/manage.py", "runserver"]
