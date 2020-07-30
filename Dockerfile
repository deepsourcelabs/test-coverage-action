FROM python:3.8.5-slim-buster
ENV PYTHONPATH /app
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ADD . /app
WORKDIR /app

# install curl
RUN apt-get update
RUN apt-get install curl

# download the DeepSource CLI binary
RUN curl https://deepsource.io/cli | sh
RUN ["chmod", "777", "/app/main.py"]

CMD ["/app/main.py"]
