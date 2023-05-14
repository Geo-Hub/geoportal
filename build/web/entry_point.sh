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

echo "Postgres server is running proceeding."
echo "-------------------------------------------------------------------"
echo "${0}: running migrations."
python manage.py makemigrations --merge --noinput --check
python manage.py migrate --noinput

echo "${0}: collecting statics."

python manage.py collectstatic --noinput

echo "Loading GIS data into the DB."
python manage.py load_gis_data

echo "Starting webserver"
gunicorn --bind 0.0.0.0:8000 geoportal.wsgi \
      --timeout 600 \
      --workers 4 \
      --log-level=debug \
      --reload