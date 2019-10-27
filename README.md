# AWS Lambda thumbnail generator

**AWS**: s3, Lambda, CloudFormation

**Other**: Python, Docker, Pillow (Python dependency)

Image file (jpg, png) uploads to s3 trigger a lambda function that automatically resizes them and saves them to the same bucket

Utilizes the [Serverless Framework](https://serverless.com/) for fast deployment
