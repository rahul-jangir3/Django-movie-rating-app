# Base image
FROM python:3.12-slim

# Set work directory
WORKDIR /app

# Prevent Python from writing .pyc files & set stdout to unbuffered
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies (for psycopg2 or pillow etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (better caching)
COPY requirements.txt /app/

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy rest of the project
COPY . /app/

# Expose Django port
EXPOSE 8000

RUN mkdir -p /app/db && chmod 777 /app/db

COPY entrypoint.sh /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
