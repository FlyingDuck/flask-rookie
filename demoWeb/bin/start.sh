#!/bin/bash

gunicorn --config=gunicorn.conf manage:app

# gunicorn --bind=:5000 --workers=2 manage:app