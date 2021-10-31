FROM python:3.9
COPY . /usr/src/myapp
WORKDIR /usr/src/myapp
CMD ["python", "app.py"]