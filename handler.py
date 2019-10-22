import boto3
from io import BytesIO
from PIL import Image, ImageOps
import os

s3 = boto3.client('s3')
""" :type : pyboto3.s3 """
size = int(os.environ['THUMBNAIL_SIZE'])


def s3_thumbnail_generator(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    print('bucket', bucket)
    print('key', key)

    print('is_thumbnail(key)', is_thumbnail(key))

    if not is_thumbnail(key):
        image = get_s3_image(bucket, key)
        print('image', image)
        thumbnail = image_to_thumbnail(image)
        print('thumbnail', thumbnail)
        thumbnail_key = new_filename(key)
        print('thumbnail_key', thumbnail_key)
        url = upload_to_s3(bucket, thumbnail_key, thumbnail)
        return url


def is_thumbnail(key):
    # TODO - can improve this so search term is last in filename
    if key.find("_thumbnail.") > -1:
        return True
    return False


def get_s3_image(bucket, key):
    resp = s3.get_object(Bucket=bucket, Key=key)
    image_content = resp['Body'].read()
    file = BytesIO(image_content)
    img = Image.open(file)
    return img


def image_to_thumbnail(image):
    dimensions = (size, size)
    return ImageOps.fit(image, dimensions)


def new_filename(key):
    split = key.rsplit('.', 1)
    base, extension = split[0], split[1]
    return f"{base}_thumbnail.{extension}"


def upload_to_s3(bucket, key, image):
    new_thumbnail = BytesIO()
    file_extension = key.rsplit('.', 1)[1]
    if file_extension == "jpg":
        file_extension = "jpeg"  # For Pillow processing
    image.save(new_thumbnail, file_extension)
    new_thumbnail.seek(0)

    response = s3.put_object(
        ACL='public-read',
        Body=new_thumbnail,
        Bucket=bucket,
        ContentType='image/'+file_extension,
        Key=key
    )
    print('response', response)

    url = f"{s3.meta.endpoint_url}/{bucket}/{key}"
    print("url", url)
