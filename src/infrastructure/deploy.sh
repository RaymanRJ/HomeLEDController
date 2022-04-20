#!/bin/bash

# Parameters:
REGION=us-east-2
STACKNAME=HomeLEDController
S3BUCKETNAME=home-led-controller
WEBAPPREPOSITORYNAME=home-led-controller

# Create temp bucket to hold artifacts
TEMPBUCKET=rrjamal-temp-$REGION
aws --region $REGION s3api create-bucket --bucket $TEMPBUCKET --create-bucket-configuration LocationConstraint=$REGION
aws --region $REGION s3api put-public-access-block --bucket $TEMPBUCKET --public-access-block-configuration \
BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true

# Build template and upload artifacts to temp bucket:
aws --region $REGION cloudformation package --template-file template.yml --output-template-file deployment.yml --s3-bucket $TEMPBUCKET

# Deploy new template:
aws --region $REGION cloudformation deploy \
    --s3-bucket $TEMPBUCKET \
    --template-file deployment.yml \
    --capabilities CAPABILITY_NAMED_IAM \
    --stack-name $STACKNAME \
    --parameter-overrides \
    S3BucketName=$S3BUCKETNAME \
    WebAppRepositoryName=$WEBAPPREPOSITORYNAME

# Cleanup - Delete the temp bucket
echo "Emptying temporary bucket and deleting..."
aws --region $REGION s3 rm s3://$TEMPBUCKET --recursive
aws --region $REGION s3api delete-bucket --bucket $TEMPBUCKET

rm deployment.yml