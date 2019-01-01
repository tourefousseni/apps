#! /bin/bash


create database plateform;
create user myprojectuser WITH PASSWORD 'password';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE plateform TO myprojectuser;
\c plateform;
create extension postgis;
python manage.py makemigrations;
python manage.py migrate;
python manage.py createsuperuser;

python manage.py dumpdata --format=json contacts > /Users/toure/PycharmProjects/douniyasoba/tmp/data1.json
python manage.py loaddata  /Users/toure/PycharmProjects/douniyasoba/tmp/data1.json

