# Toystori v2

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/b03ea0563d9d49ccaa12713d61989ceb)](https://www.codacy.com/app/caulagi/v2?utm_source=github.com&utm_medium=referral&utm_content=toystori/v2&utm_campaign=badger)
[![Build Status](https://travis-ci.org/toystori/v2.svg?branch=master)](https://travis-ci.org/toystori/v2)


## Development setup


#### Database setup

```bash
# use the docker image for postgres with postgis
$ docker volume create pgdata
$ docker run \
    -v pgdata:/var/lib/postgresql/data \
    -e POSTGRES_PASSWORD=1234 \
    -e POSTGRES_DB=toystori_dev \
    -p 5432:5432 \
    -d mdillon/postgis:9.6-alpine
```

#### Running application with docker

```bash
$ docker build -t toystori-v2 .

# docker for mac
$ export HOSTIP=192.168.65.1

# linux
$ export HOSTIP=127.0.0.1

$ docker run  --add-host=docker:${HOSTIP} -p 9090:9090 --rm -it toystori-v2
```

**Note** - See the application [here](http://localhost:9090/)

#### Running application locally

The recommended python version is **3.6.1**

```
$ python3 -m venv ~/.venv/toystori
$ . ~/.venv/toystori/bin/activate
$ pip install -r requirements/dev.txt

# Install GeoDjango dependencies
$ brew install gdal libgeoip

$ python app/manage.py runserver
```

### Tests

Tests are run with py.test. 

```bash
# run with output
$ py.test -s

# run with coverage (used by ci)
py.test --cov-report xml --cov .
```
