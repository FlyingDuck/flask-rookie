#!/bin/bash

gunicorn --config=gunicorn.conf wsgi:app

# gunicorn --bind=:5000 --workers=2 wsgi:app