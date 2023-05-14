#!/bin/bash

set -e
# ensure the postgress server is running.
echo "Checking status for postgres server."
db_connection_test=1
while [ $db_connection_test -eq 1 ]
do
    set +e
    python db_connection_test.py
    db_connection_test=$?
    set -e
    echo test result: $db_connection_test
    sleep 1
done

echo "${0}: running migrations."
python manage.py makemigrations --merge
python manage.py migrate --noinput

#echo "${0}: collecting statics."
#
#python manage.py collectstatic --noinput

python manage.py load_gis_data

gunicorn --bind 0.0.0.0:8000 geoportal.wsgi

# gunicorn yourapp.wsgi:application \
#     --env DJANGO_SETTINGS_MODULE=yourapp.production_settings \
#     --name yourapp \
#     --bind 0.0.0.0:8000 \
#     --timeout 600 \
#     --workers 4 \
#     --log-level=info \
#     --reload
