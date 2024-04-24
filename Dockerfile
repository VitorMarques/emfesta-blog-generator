FROM python:3.11.0-alpine

WORKDIR /app

RUN apk update && apk add --no-cache \
    gcc \
    g++ \
    make \
    libffi-dev \
    openssl-dev \
    musl-dev \
    cargo \
    linux-headers \
    py3-pip

RUN pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock* /app/

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY . /app

EXPOSE 5000

CMD ["python", "main.py"]
