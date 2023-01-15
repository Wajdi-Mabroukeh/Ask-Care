FROM python:3.8.5


ADD ./requirements.txt /app/requirements.txt

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt

ADD . /app
WORKDIR /app

RUN python manage.py migrate --noinput \
    && python manage.py collectstatic --noinput

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE 'settings.base'
ENV VERSION 1
ENV SERVICE_ENV 'dev'

#RUN chmod +x /app/commands.sh



EXPOSE 8001
#"--workers", "4",
# "0.0.0.0:8000"
# Start the Gunicorn server
CMD ["gunicorn", "--bind", ":8001", "--workers", "2", "--keep-alive", "60", "--timeout", "60" ,"settings.wsgi:application"]