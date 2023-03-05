FROM python:3.11-slim

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

WORKDIR /app
COPY requirements.txt  /app


RUN pip install --no-cache-dir -r requirements.txt

COPY start.django.sh /start-django
RUN chmod +x /start-django

ADD .. /app/