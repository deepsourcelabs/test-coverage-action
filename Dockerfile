FROM python:3.8.5-slim-buster
ENV PYTHONPATH /app
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ADD . /app
WORKDIR /app

# download the DeepSource CLI binary
RUN curl https://deepsource.io/cli | sh

CMD ["/app/main.py"]
