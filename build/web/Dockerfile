FROM ghcr.io/osgeo/gdal:ubuntu-full-3.6.4

WORKDIR /app

COPY web/get-pip.py ./
COPY web/requirements.txt ./
RUN python get-pip.py
RUN pip3 install -r requirements.txt

COPY web ./

RUN unzip data.zip -d /app/main/management/load_scripts/

COPY build/web/entry_point.sh /app/entry_point.sh
RUN chmod +x /app/entry_point.sh
