# AWS Lambda thumbnail generator

Image file (jpg, png) uploads to s3 trigger a lambda function that automatically resizes them and saves it to the same bucket

Utilizes the [Serverless Framework](https://serverless.com/) for fast deployment.

AWS services: s3, Lambda, CloudFormation

Other: Docker, Pillow (Python dependency)

