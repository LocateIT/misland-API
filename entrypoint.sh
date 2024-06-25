#!/bin/bash

case "$1" in
    develop)
        echo "Running Development Server"
        FLASK_APP=main.py flask db upgrade
        exec python main.py
        ;;
    test)
        echo "Test (not yet)"
        ;;
    start)
        echo "Running Start"
        FLASK_APP=main.py flask db upgrade
        exec gunicorn -c gunicorn.py misland_api.wsgi:application
        ;;
    worker)
        echo "Running celery"
        exec celery -A misland_api.celery worker -E -B --loglevel=DEBUG
        ;;
    *)
        exec "$@"
esac
