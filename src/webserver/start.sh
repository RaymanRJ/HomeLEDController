#!/bin/bash

# This script will deploy to the webserver machine. It will create a cronjob
# to check for updates to the image periodically.
# Once an update is detected, the job will download the new image,
# kill the live one, and start the new image.

IMAGE_NAME=$AWSACCOUNT.dkr.$AWSREGION.amazonaws.com/$AWSREPO:development

# Start image:
sudo docker run -d -p 0.0.0.0:5000:5000 -v /app/web-server-data:/app/web-server-data/ $IMAGE_NAME
