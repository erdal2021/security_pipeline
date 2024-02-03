FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y \
    wget \
    curl \
    python3 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

RUN chmod -R 755 /app

CMD ["python3", "run.py"]
