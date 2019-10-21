import boto3
import cStringIO
import os

s3 = boto3.client('s3')
size = int(os.environ['THUMBNAIL_SIZE'])


def s3_thumbnail_generator(event, context):
    print(event)

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['bucket']['key']

    if not key.endswith("_thumbnail.png"):
        image = get_s3_image(bucket, key)
        thumbnail = image_to_thumbnail(image)


def get_s3_image(bucket, key):
    resp = s3.get_object(Bucket=bucket, Key=key)
    image_content = resp['Body'].read()
    file = cStringIO.StringIO(image_content)
    


def image_to_thumbnail(image):
    return

