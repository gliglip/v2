# v2

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/b03ea0563d9d49ccaa12713d61989ceb)](https://www.codacy.com/app/caulagi/v2?utm_source=github.com&utm_medium=referral&utm_content=toystori/v2&utm_campaign=badger)
[![Build Status](https://travis-ci.org/toystori/v2.svg?branch=master)](https://travis-ci.org/toystori/v2)


## Development setup

The recommended python version is 3.6.1

```
$ python3 -m venv ~/.venv/toystori
$ . ~/.venv/toystori/bin/activate
$ pip install -r requirements/dev.txt

# Install GeoDjango dependencies
$ brew install gdal libgeoip

# use the docker image for postgres with postgis
$ docker volume create pgdata
$ docker run \
    -v pgdata:/var/lib/postgresql/data \
    -e POSTGRES_PASSWORD=1234 \
    -e POSTGRES_DB=toystori_dev \
    -p 5432:5432 \
    -d mdillon/postgis:9.6-alpine

$ python manage.py runserver
```

### Tests

Tests are run with py.test. 

```
$ make test

$ py.test --cov .
```
