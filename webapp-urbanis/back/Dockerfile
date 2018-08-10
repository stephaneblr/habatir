FROM python:2.7.15
WORKDIR /usr/src/app

#RUN apt-get update && apt-get install -y python-pip python-dev build-essential
RUN pip install --upgrade pip
RUN pip install --upgrade virtualenv
RUN pip install Flask Flask-Cors Flask-MySQL Flask-RESTful

COPY . .

ENV FLASK_APP=./api.py

EXPOSE 5000

CMD flask run --host=0.0.0.0