#!/usr/bin/env bash
python3 manage.py migrate;
create database kaladb;
create user myprojectuser WITH PASSWORD 'password';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE kaladb TO myprojectuser;