import boto3
import json
import ast
from io import BytesIO

#set up S3 Client
s3Client = boto3.client('s3')
s3 = boto3.resource('s3')
f = BytesIO()
bucket_name = "sezzlecalculatorbucket"
file_name = "output.json"

#Retrieves the calculation file from S3,
#Adds the calculation to the S3 file,
#evicts oldest calculation if the number
#of saved calculations exceeds 10
class Cache:
    def addCalc(self, calc):
        object = s3.Object(bucket_name, file_name)
        s3Client.download_fileobj(bucket_name, file_name, f)
        val = ast.literal_eval((f.getvalue()).decode('utf-8'))
        results = val['results']
        results.append(calc)
        if(len(results) > 10):
            results.pop(0)
        body = {
            "results" : results
        }
        object.put(Body=json.dumps(body))
    