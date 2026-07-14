aws login | aws ecr get-login-password --region eu-north-1 | docker login --username AWS --password-stdin 683210040241.dkr.ecr.eu-north-1.amazonaws.com 

docker build -t data-collector -f data_collector/Dockerfile .
# Replace repository with other repository if you want to push to a different one
docker tag meat_scraper:latest 683210040241.dkr.ecr.eu-north-1.amazonaws.com/meatscraper/meat_scraper:latest 
# Publish the image to ECR
docker push 683210040241.dkr.ecr.eu-north-1.amazonaws.com/meatscraper/meat_scraper:latest 