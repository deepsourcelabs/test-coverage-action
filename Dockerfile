FROM python:3.8.5-slim-buster AS builder
ADD . /app
WORKDIR /app

# download the DeepSource CLI binary
RUN curl https://deepsource.io/cli | sh
# TODO

FROM gcr.io/distroless/python3
COPY --from=builder /app /app
WORKDIR /app
ENV PYTHONPATH /app
CMD ["/app/main.py"]
