#! /bin/bash
#python manage.py dumpdata --format=json accounts > /Users/toure/PycharmProjects/douniyasoba/tmp/$(date +"%Y%m%d_%H:%M:%S")_data.json;
python manage.py dumpdata --format=json contacts > /Users/foussenytoure/Documents/ProjectPycharm/douniyasoba/tmp/$(date +"%Y%m%d_%H:%M:%S")_data.json;
psql -U postgresql;
drop database kaladb;
CREATE database kaladb;
CREATE user myprojectuser WITH PASSWORD 'password';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE kaladb TO myprojectuser;
\c kaladb;
CREATE extension postgis;
CREATE EXTENSION postgis_topology;
python manage.py makemigrations;
python manage.py migrate;
python manage.py createsuperuser;
python manage.py loaddata  /Users/foussenytoure/Documents/ProjectPycharm/douniyasoba/tmp/$(current +"%Y%m%d_%H:%M:%S")_data.json;
