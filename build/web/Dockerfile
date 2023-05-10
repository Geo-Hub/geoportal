FROM ghcr.io/osgeo/gdal:ubuntu-full-3.6.4

WORKDIR /app

COPY web .

RUN apt update
RUN apt install python3-pip -y
RUN pip3 install -r requirements.txt

RUN python manage.py migrate

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "geoportal.wsgi"]
