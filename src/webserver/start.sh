#!/bin/bash

# This script will deploy to the webserver machine. It will create a cronjob
# to check for updates to the image periodically.
# Once an update is detected, the job will download the new image,
# kill the live one, and start the new image.

echo """
#!/bin/sh

AWSACCOUNT=<<AWSACCOUNT>>
AWSREGION=<<AWSREGION>>
AWSREPO=home-led-controller

aws ecr get-login-password --region \$AWSREGION | docker login --username AWS --password-stdin \$AWSACCOUNT.dkr.ecr.\$AWSREGION.amazonaws.com

IMAGE_NAME=\"\$AWSACCOUNT.dkr.ecr.\$AWSREGION.amazonaws.com/\$AWSREPO:development\"

LIVE_IMAGE=\"\$(sudo docker image inspect \"\$IMAGE_NAME\" | jq '.[0].\"RepoDigests\"[0]')'\"

LATEST_IMAGE_SHA=\"\$(aws ecr describe-images --repository-name \$AWSREPO | jq '.imageDetails[0].imageDigest' | tr -d '\"')\"
LATEST_IMAGE=\"\$AWSACCOUNT.dkr.ecr.\$AWSREGION.amazonaws.com/\$AWSREPO@\$LATEST_IMAGE_SHA\"

echo \"LIVEIMAGE   =\$LIVE_IMAGE\"
echo \"LATEST_IMAGE=\$LATEST_IMAGE\"

if [ \$LIVE_IMAGE = \$LATEST_IMAGE ]
then
    echo "Image is current."
    exit 0
fi

echo "Image needs to be updated."

sudo docker pull \$IMAGE_NAME

# If multiple containers will be running on the machine, this will have to be redone:
LIVE_CONTAINER=\$(sudo docker ps -q)
sudo docker kill \$LIVE_CONTAINER

# Start new image:
sudo docker run -d -p 0.0.0.0:5000:5000 -v /app/web-server-data:/app/web-server-data/ \$IMAGE_NAME

""" > update-web-server.sh

echo "*/5 * * * * sh $(pwd)/update-web-server.sh >> $(pwd)/update-web-server.log 2>&1" > update-cron
crontab update-cron