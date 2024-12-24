FROM python:3-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install mc (MinIO Client)
RUN apt-get update && apt-get install -y curl && \
    curl -O https://dl.min.io/client/mc/release/linux-amd64/mc && \
    chmod +x mc && \
    mv mc /usr/bin/mc

# Copy the uploader script
COPY uploader.py uploader.py

# Command to start the container
CMD \
    echo "Waiting for MinIO to be ready..." && \
    until mc alias set myminio http://minio:9000 $MINIO_ACCESS_KEY $MINIO_SECRET_KEY; do sleep 5; done && \
    mc mb myminio/test-bucket && \
    mc quota set myminio/test-bucket --size 90mib && \
    python uploader.py
