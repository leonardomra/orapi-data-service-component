import logging
import boto3
from botocore.exceptions import ClientError

class S3Handler():
    
    def __init__(self, AWS_REGION=None, AWS_ACCESS_KEY=None, AWS_SECRET_KEY=None):
        self.awsRegion = AWS_REGION
        self.awsAccessKey = AWS_ACCESS_KEY
        self.awsSecretKey = AWS_SECRET_KEY
        self.s3 = boto3.client(
            's3',
            region_name=AWS_REGION,
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY
        )
        self.s3Resource = boto3.resource('s3',
        region_name=AWS_REGION,
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY)
    
    def createBucket(self, bucket_name):  
        try:
            location = {'LocationConstraint': self.awsRegion}
            self.s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
        except ClientError as e:
            logging.error(e)
            return False
        return True

    def listBuckets(self):
        response = self.s3.list_buckets()
        # Output the bucket names
        print('Existing buckets:', flush=True)
        for bucket in response['Buckets']:
            print(f'  {bucket["Name"]}', flush=True)
        buckets = [bucket['Name'] for bucket in response['Buckets']]
        return buckets

    def uploadFile(self, bucket_name, filename):
        try:
            self.s3.upload_file(filename, bucket_name, filename)
        except ClientError as e:
            logging.error(e)
            return False
        return True
    
    def uploadFileObject(self, data, bucket_name, filename):
        useResource = True
        if useResource:
            try:
                self.s3Resource.Object(bucket_name, filename).put(Body=data)
            except ClientError as e:
                logging.error(e)
                return False
        else:
            try:
                self.s3.put_object(Body=data, Bucket=bucket_name, Key=filename)
            except ClientError as e:
                logging.error(e)
                return False  
        return True
        