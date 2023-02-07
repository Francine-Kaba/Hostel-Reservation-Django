FROM python:3.8-slim-buster AS python
WORKDIR /usr/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
COPY requirements.txt /usr/app/requirements.txt
RUN pip install -r requirements.txt
RUN pip install django-prometheus
COPY . .
RUN python manage.py makemigrations
RUN python manage.py migrate
EXPOSE 8000
# run python program
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]