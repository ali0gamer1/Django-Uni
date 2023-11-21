
FROM python:3.8
WORKDIR /daneshgah
COPY . /daneshgah
RUN pip install -r requirements.txt
EXPOSE 8080
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput
ENV DJANGO_SETTINGS_MODULE=daneshgah.settings
CMD ["gunicorn", "daneshgah.wsgi:application", "--bind", "0.0.0.0:8000"]
