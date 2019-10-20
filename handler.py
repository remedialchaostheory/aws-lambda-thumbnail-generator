import boto3
import os

s3 = boto3.client('s3')
size = int(os.environ['THUMBNAIL_SIZE'])


