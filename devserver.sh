#!/bin/sh
source .venv/bin/activate
python backend/manage.py runserver 0.0.0.0:$PORT
