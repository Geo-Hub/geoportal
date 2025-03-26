FROM ghcr.io/osgeo/gdal:alpine-small-3.6.3

WORKDIR /app

# install python and requirements
RUN apk add --no-cache python3 py3-pip py3-virtualenv python3-dev libpq bash geos unzip

# create a virtual env
RUN python3 -m venv venv

COPY web/build/requirements.txt requirements.txt
RUN venv/bin/python -m pip install -r requirements.txt

COPY web/build/db_connection_test.py .
COPY web/build/entry_point.sh .
RUN chmod +x entry_point.sh

COPY web ./

ENTRYPOINT ["bash", "/app/entry_point.sh"]
