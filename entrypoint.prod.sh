#!/bin/bash

python manage.py collectstatic --noinput
python manage.py migrate --no-input
gunicorn myDjangoBlog.wsgi -b 0.0.0.0:8000 --timeout 900 --chdir=/code --log-level debug --log-file -
exec "$@"
