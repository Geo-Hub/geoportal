FROM ghcr.io/osgeo/gdal:ubuntu-full-3.6.4

WORKDIR /app

COPY web .

RUN apt update
RUN apt install python3-pip -y
RUN pip3 install -r requirements.txt

COPY build/web/entry_point.sh /app/entry_point.sh
RUN chmod +x /app/entry_point.sh
