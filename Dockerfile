FROM python:3.9.23-slim-bookworm
ENV PYTHONPATH /app
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN groupadd --gid 5000 main \
    && useradd --home-dir /home/main --create-home --uid 5000 \
        --gid 5000 --shell /bin/sh --skel /dev/null main

COPY . /app
WORKDIR /app

# install curl; skipcq: DOK-DL3008
RUN apt-get update && apt-get install --no-install-recommends -y curl git && apt-get clean && rm -rf /var/lib/apt/lists/*
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# download the DeepSource CLI binary
RUN curl https://deepsource.io/cli | bash
RUN ["chmod", "777", "/app/main.py"]

USER main

CMD ["/app/main.py"]
