FROM ghcr.io/osgeo/gdal:ubuntu-full-3.6.4

WORKDIR /app

COPY web .

RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py
RUN pip3 install -r requirements.txt

COPY build/web/entry_point.sh /app/entry_point.sh
RUN chmod +x /app/entry_point.sh
