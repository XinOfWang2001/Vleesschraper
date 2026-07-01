# FROM python:3.12-slim
FROM python:3.12-alpine
WORKDIR /app

# Set environmental variables that are set outside of the image.
# ENV FILES="Xin"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 1. Copy requirements from the root context
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# 2. Copy the src folder from the root context
COPY src/ ./src/

# 3. Copy the data_collector application files
COPY data_collector/ .

EXPOSE 80

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80"]