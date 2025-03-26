#!/bin/bash

set -e

# ensure the postgress server is running.
echo "Checking status for postgres server."
db_connection_test=1
num_retries=0
while [ $db_connection_test -eq 1 ] && [ $num_retries -lt 10 ]
do
    set +e
    venv/bin/python db_connection_test.py
    db_connection_test=$?
    set -e
    num_retries=$((num_retries + 1))
    echo test result: $num_retries failed
    sleep 1
done

if [ $db_connection_test -eq 1 ]
then
    echo "Postgres server is not running after $num_retries retries."
    exit 1
fi

echo "Postgres server is running proceeding."
echo "-------------------------------------------------------------------"
echo "${0}: running migrations."
venv/bin/python manage.py makemigrations --merge --noinput --check
venv/bin/python manage.py migrate --noinput

echo "${0}: collecting statics files."

venv/bin/python manage.py collectstatic --noinput

echo "Loading GIS data into the DB."
unzip data.zip -d /app/main/management/load_scripts/
venv/bin/python manage.py load_gis_data

rm -rf /app/main/management/load_scripts/data
rm data.zip

echo "Starting webserver"
if [ "$DEBUG" == "True" ]; then
    venv/bin/python manage.py runserver 0.0.0.0:8000
else
    venv/bin/python -m gunicorn --bind 0.0.0.0:8000 geoportal.wsgi
fi
