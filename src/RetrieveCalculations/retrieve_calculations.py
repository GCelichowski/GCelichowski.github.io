import json
import ast
import boto3
from io import BytesIO

#set up S3 client, other constants
s3Client = boto3.client('s3')
s3 = boto3.resource('s3')
f = BytesIO()
bucket_name = "sezzlecalculatorbucket"
file_name = "output.json"

#retrieve calculations JSON from S3 and return it
def lambda_handler(event, context):
    try:
        s3Client.download_fileobj(bucket_name, file_name, f)
        val = ast.literal_eval((f.getvalue()).decode('utf-8'))
        results = val['results']
        return {
            'statusCode': 200,
            'calculation': results
        }
    except:
        return {
            'statusCode' : 500,
            'errorMessage' : "unknown server error"
        }
