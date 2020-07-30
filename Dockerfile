FROM python:3.8.5-slim-buster
ENV PYTHONPATH /app
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY . /app
WORKDIR /app

# install curl; skipcq: DOK-DL3008
RUN apt-get update && apt-get install -y curl git && apt-get clean && rm -rf /var/lib/apt/lists/*
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# download the DeepSource CLI binary
RUN curl https://deepsource.io/cli | bash
RUN ["chmod", "777", "/app/main.py"]

CMD ["/app/main.py"]
