#!/bin/bash

# Set AWS instance IP address and other variables
#AWS_INSTANCE_IP="34.230.161.156"
DOCKER_IMAGE_NAME="recipies"
DOCKER_IMAGE_TAG="latest"
REPOSITORY_NAME="recipies"

#Docker login
docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD

# Build the Docker image
docker build -f recipies/Dockerfile -t gburucua/recipies:latest .

# Push the Docker image to a registry (e.g., Docker Hub)
docker push gburucua/recipies:latest