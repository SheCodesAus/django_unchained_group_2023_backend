#!/usr/bin/env bash
python manage.py migrate
python manage.py createsuperuser --no-input
gunicorn --bind :8000 --workers 1 buybuddy.wsgi