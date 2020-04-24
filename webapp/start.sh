#!/usr/bin/env bash

run setup.py

set -x -e

gunicorn --bind=0.0.0.0:5000 --keep-alive=2000 \
    --timeout=2000 --log-level=debug  --reload \
    flaskapp:app
