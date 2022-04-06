"""
This module contains all the logic required for storing images
"""

from firebase_admin import storage

def store_image(file,file_name) -> str:
    """
    Stores an image file with a given file name.
    """

    temp_file_name = file_name+'.jpg'
    bucket_url = 'ecommerce-68ba8.appspot.com'

    with open(temp_file_name, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
            
    storage_bucket = storage.bucket(bucket_url)
    blob = storage_bucket.blob(temp_file_name)
    blob.upload_from_filename(temp_file_name)
    blob.make_public()

    return blob.public_url

def get_image_url(file_name):
    """
    Gets an image file that is sotred with the given file name.
    """
    temp_file_name = file_name+'.jpg'
    bucket_url = 'ecommerce-68ba8.appspot.com'

    storage.bucket(bucket_url).get_blob(temp_file_name)
