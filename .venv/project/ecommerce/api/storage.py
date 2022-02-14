from firebase_admin import credentials, initialize_app, storage

def store_image(file) -> str:

    tempFileName = 'temp.jpg'
    bucketURL = 'ecommerce-68ba8.appspot.com'

    with open(tempFileName, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
            
    storageBucket = storage.bucket(bucketURL)
    blob = storageBucket.blob(tempFileName)
    blob.upload_from_filename(tempFileName) 
    blob.make_public()

    return blob.public_url