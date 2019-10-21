import boto3
from io import BytesIO
from PIL import Image
import os

s3 = boto3.client('s3')
size = int(os.environ['THUMBNAIL_SIZE'])


def s3_thumbnail_generator(event, context):
    print(event)

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    if not key.endswith("_thumbnail.png"):
        image = get_s3_image(bucket, key)
        print('image', image)
        thumbnail = image_to_thumbnail(image)
        print('thumbnail', thumbnail)


def get_s3_image(bucket, key):
    resp = s3.get_object(Bucket=bucket, Key=key)
    image_content = resp['Body'].read()
    file = BytesIO(image_content)
    img = Image.open(file)
    return img


def image_to_thumbnail(image):
    dimensions = (size, size)
    return image.thumbnail(dimensions)

