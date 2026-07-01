docker build -t data-synchronizer -f data_synchronizer/Dockerfile .
# Replace repository with other repository if you want to push to a different one
docker tag synchronizer:latest 683210040241.dkr.ecr.eu-north-1.amazonaws.com/meatscraper/data-synchronizer:latest 
# Publish the image to ECR
docker push 683210040241.dkr.ecr.eu-north-1.amazonaws.com/meatscraper/synchronizer:latest 