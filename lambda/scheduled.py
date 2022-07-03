import boto3
import json

s3 = boto3.client("s3")


def lambda_handler(event, context):
    print(event)


"""
event
{
   "version":"0",
   "id":"b238c452-b270-c517-c8ed-fce6bb01a5a3",
   "detail-type":"Scheduled Event",
   "source":"aws.events",
   "account":"656169322665",
   "time":"2022-07-03T07:00:00Z",
   "region":"ap-northeast-1",
   "resources":[
      "arn:aws:events:ap-northeast-1:656169322665:rule/CdkS3NotifyPrefixStack-Rule4C995B7F-Z9A8T4QOZQVJ"
   ],
   "detail":{
      
   }
}
"""
