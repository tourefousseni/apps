#! /bin/bash


create database plateform;
create user myprojectuser WITH PASSWORD 'password';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE plateform TO myprojectuser;
\c plateform;
create extension postgis;

python manage.py dumpdata --format=json contacts > /tmp/data2.json
python manage.py loaddata  /tmp/data2.json

