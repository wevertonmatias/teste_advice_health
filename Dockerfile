FROM python:3

WORKDIR /app
ADD    ./requirements.txt   /app/
RUN    pip install -r requirements.txt

ADD    ./carford   /app/carford/
ADD    ./gunicorn       /app/gunicorn/
ADD    ./manage.py      /app/
