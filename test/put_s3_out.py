import boto3
import os
import json

s3 = boto3.client("s3")

json_s3key = os.path.join("foo1", "hello") + ".json"

json_response = s3.put_object(
    Bucket=os.environ.get("BUCKET_NAME"), Key=json_s3key, Body=json.dumps({"A": 1})
)
