# Use the Python3.7.2 container image
FROM python:3.7.2-stretch

WORKDIR /app

ADD . /app

# Install the dependencies
RUN pip install -r requirements.txt

CMD ["uwsgi", "app.ini"]