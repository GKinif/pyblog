# djangoRest

## Install dependencies

> poetry install

## Migrate Database

> poetry run manage.py migrate

## Run development server

> poetry run manage.py runserver

## Create super user

> poetry run manage.py createsuperuser

## Create new app

> poetry run django-admin.py startapp [app name]

## Create new migration

> poetry run manage.py makemigrations [app name]

## Add a new python dependency

> poetry add [package]


## Docker Compose django postgres

> https://docs.docker.com/samples/django/

## Enable trigram similarity full text search in postgres

> - psql blog
> - CREATE EXTENSION pg_trgm;

## Source

Django 3 by Example

> https://learning.oreilly.com/library/view/django-3-by/9781838981952/

