FROM python:3.9.7-slim-buster

RUN python -m pip install pip==21.3.1

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY flask-application /app
WORKDIR /app

RUN ls
RUN pwd

EXPOSE 80

CMD ["gunicorn", "--bind=0.0.0.0:80", "--workers=4", "--timeout=500", "--threads=1", "run:app"]
