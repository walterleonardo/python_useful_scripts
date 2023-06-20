from minio import Minio
#from dotenv import load_dotenv
import os
#load_dotenv()

bucket_name = 'bucket-s3'
bucket_host = 'bucket.walii.es'
local_file = 'example.png'
access_key = ''
secret_key = ''



LOCAL_FILE_PATH = os.environ.get('LOCAL_FILE_PATH', local_file)
ACCESS_KEY = os.environ.get('ACCESS_KEY', access_key)
SECRET_KEY = os.environ.get('SECRET_KEY', secret_key)
MINIO_API_HOST = "{}:9000".format(bucket_host)

print(MINIO_API_HOST)


MINIO_CLIENT = Minio(MINIO_API_HOST, access_key=ACCESS_KEY, secret_key=SECRET_KEY, secure=False)
def main():
    found = MINIO_CLIENT.bucket_exists(bucket_name)
    if not found:
        MINIO_CLIENT.make_bucket(bucket_name)
    else:
        print("Bucket already exists")
    MINIO_CLIENT.fput_object(bucket_name, local_file, LOCAL_FILE_PATH)
    print("It is successfully uploaded to bucket")



main()