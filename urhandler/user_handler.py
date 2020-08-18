import boto3

class UserHandler():
    
    def __init__(self, AWS_REGION=None, AWS_ACCESS_KEY=None, AWS_SECRET_KEY=None):
        self.awsRegion = AWS_REGION
        self.awsAccessKey = AWS_ACCESS_KEY
        self.awsSecretKey = AWS_SECRET_KEY
        self.cg = boto3.client(
            'cognito-idp',
            region_name=AWS_REGION,
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY
        )

    def getUser(self, userPoolId, username):
        return self.cg.admin_get_user(
            UserPoolId=userPoolId,
            Username=username
        )