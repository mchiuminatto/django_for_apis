FROM python:3.11

LABEL authors="mchiuminatto"

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt --upgrade pip

COPY . code
WORKDIR /code
EXPOSE 8000

CMD ["gunicorn" , "--bind", "0.0.0.0:8000", "django_project.wsgi"]