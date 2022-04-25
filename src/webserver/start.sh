#!/bin/bash

# TODO: Instead of building, we should be pulling new images from ECR
# Build image:
sudo docker build -t web-server .

# Start container:
sudo docker run -d -p 0.0.0.0:5000:5000 -v /app/web-server-data:/app/web-server-data/ web-server
