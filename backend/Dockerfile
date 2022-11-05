FROM python:3.11-buster AS server-base

ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && \
    apt-get install --no-install-recommends -y \
        python3-cryptography build-essential python-dev postgresql-client postgis postgresql-postgis nano gdal-bin && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade pip uwsgi
RUN apt-get update && apt-get install -y gettext && apt-get clean && rm -rf /var/lib/apt/lists/

WORKDIR /srv/server/

COPY requirements.txt /srv/server/requirements.txt

RUN mkdir -p /srv/var/
RUN touch /srv/var/main.log
RUN touch /srv/var/delivery.log

RUN pip install --no-cache-dir -r requirements.txt

COPY . /srv/server/

FROM server-base AS server

ENTRYPOINT ["sh", "./scripts/server-entrypoing.sh"]