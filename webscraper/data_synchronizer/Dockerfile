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

EXPOSE 80

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80"]