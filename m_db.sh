#!/usr/bin/env bash
python3 manage.py makemigrations && python manage.py migrate && python manage.py createsuperuser