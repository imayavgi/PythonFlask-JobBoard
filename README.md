# Setup

## Create Virtual Environment
python -m venv venv
pip install -r requirements.txt

## Run application using flask
Make sure .env is present in root of project dir (FLASK=APP=jobs.app, FLASK_ENV=dev)
flask run

## Run application using gunicron
pip install gunicorn

## any one of these methods
gunicorn jobs.app:app
gunicorn -w 4 -b 127.0.0.1:8888 jobs.app:app
gunicorn wsgi:app