#!/usr/bin/env bash
set -o errexit
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate --noinput

# Seulement si activé temporairement dans Render :
if [ "${CREATE_DEMO_ADMIN:-0}" = "1" ]; then
    python manage.py createsuperuser --noinput
fi
