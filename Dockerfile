FROM python:3.9
COPY . /usr/src/myapp
WORKDIR /usr/src/myapp
RUN set GOOGLE_APPLICATION_CREDENTIALS=docker-327322-8600d88d9e6e
CMD ["python", "app.py"]