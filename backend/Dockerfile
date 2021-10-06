# syntax=docker/dockerfile:1

FROM python:3.9-buster

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN apt-get update && apt-get install nano \
    && addgroup appgroup && adduser --ingroup appgroup --disabled-password appuser \
    && rm /bin/sh && ln -s /bin/bash /bin/sh \
    && mkdir /app && pip install --upgrade pip \
    && pip install -r /requirements.txt

COPY --chown=appuser:appgroup ./app /app

WORKDIR /app

# Switching to a non-root user
USER appuser

# run gunicorn
CMD gunicorn app.wsgi:application --bind 0.0.0.0:$PORT