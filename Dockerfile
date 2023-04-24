FROM python:3.7.7-stretch AS BASE

RUN apt-get update && \
    apt-get --assume-yes --no-install-recommends install \
    build-essential \
    curl \
    git \
    jq \
    libgomp1 \
    vim

WORKDIR /app

# upgrade pip version
RUN pip install --no-cache-dir --upgrade pip

RUN pip install rasa

ADD config.yml /app/config.yml
ADD domain.yml /app/domain.yml
ADD credentials.yml /app/credentials.yml
ADD endpoints.yml /app/endpoints.yml
