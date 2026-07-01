# Build up docker image
docker build -t meat-scraper -f data_collector/Dockerfile .
# Replace repository with other repository if you want to push to a different one
docker tag meat-scraper:latest 683210040241.dkr.ecr.eu-north-1.amazonaws.com/meatscraper/fastapi-serverless:latest 
# Publish the image to ECR
docker push 683210040241.dkr.ecr.eu-north-1.amazonaws.com/meatscraper/fastapi-serverless:latest 
