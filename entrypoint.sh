#!/bin/sh
# entrypoint.sh — run migrations before starting Gunicorn

echo "Running database migrations..."
python manage.py migrate --noinput

echo "Starting Gunicorn..."
gunicorn movie_project.wsgi:application --bind 0.0.0.0:8000

