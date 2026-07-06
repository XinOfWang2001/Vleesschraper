FROM python:3.12-slim

WORKDIR /app

RUN echo "Hello world!!"

# 1. Copy requirements from the root context
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2. Copy the src folder from the root context
COPY src/ ./src/

# 3. Copy the data_collector application files
COPY data_synchronizer/ .

# Run job for AWS Fargate task. The job will run and exit after completion.
CMD ["python", "api.py"]