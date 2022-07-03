import boto3
import json

s3 = boto3.client("s3")


def lambda_handler(event, context):
    print(event)
    for record in event["Records"]:
        key = record["s3"]["object"]["key"]
        bucket = record["s3"]["bucket"]["name"]
        response = s3.get_object(Bucket=bucket, Key=key)
        print(json.loads(response["Body"].read()))


"""
event
{
   "Records":[
      {
         "eventVersion":"2.1",
         "eventSource":"aws:s3",
         "awsRegion":"ap-northeast-1",
         "eventTime":"2022-07-03T06:27:50.229Z",
         "eventName":"ObjectCreated:Put",
         "userIdentity":{
            "principalId":"AWS:AIDAIRGQRKVJ6LFTAV2U2"
         },
         "requestParameters":{
            "sourceIPAddress":"35.78.72.215"
         },
         "responseElements":{
            "x-amz-request-id":"M3GXH7G0183JW3DA",
            "x-amz-id-2":"C1qQMdkZHIGA7sE3JixIguyiBquKDhGQp/lanSIjAqbw5jVM6mMYb3aso/wz6/0Kp8nnwSL7Fv2w7EC2BYYdRIfYZ3xnEiMi"
         },
         "s3":{
            "s3SchemaVersion":"1.0",
            "configurationId":"NzdjODkyZDItYTc2Mi00NzA4LWE1NDItY2Y2ODkyNzg3NDBh",
            "bucket":{
               "name":"cdks3notifyprefixstack-bucket83908e77-2ilyz10decix",
               "ownerIdentity":{
                  "principalId":"A3IE8ALDKUHMWU"
               },
               "arn":"arn:aws:s3:::cdks3notifyprefixstack-bucket83908e77-2ilyz10decix"
            },
            "object":{
               "key":"foo/hello.json",
               "size":8,
               "eTag":"db7a0e01e367aeb00150af1316da0f82",
               "sequencer":"0062C136E63154C982"
            }
         }
      }
   ]
}
"""
