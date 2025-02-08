#!/bin/bash

uv run python sigb/manage.py makemigrations --noinput &&
uv run python sigb/manage.py migrate --noinput

exec "$@"
