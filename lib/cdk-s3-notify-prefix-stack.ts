import { Stack, StackProps, CfnOutput } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as s3n from 'aws-cdk-lib/aws-s3-notifications';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as events from 'aws-cdk-lib/aws-events';
import * as targets from 'aws-cdk-lib/aws-events-targets';

export class CdkS3NotifyPrefixStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);
    
    const bucket = new s3.Bucket(this, 'Bucket');
    
    const func = new lambda.Function(this, 'Function', {
      code: lambda.Code.fromAsset('lambda'),
      runtime: lambda.Runtime.PYTHON_3_9,
      handler: 'putevent.lambda_handler'
    })
    
    bucket.addEventNotification(s3.EventType.OBJECT_CREATED_PUT, new s3n.LambdaDestination(func), {
      prefix: 'foo/',
      suffix: '.json'
    })
    
    bucket.grantRead(func)
    
    const evfunc = new lambda.Function(this, 'FunctionEv', {
      code: lambda.Code.fromAsset('lambda'),
      runtime: lambda.Runtime.PYTHON_3_9,
      handler: 'scheduled.lambda_handler'
    })
    
    const rule = new events.Rule(this, 'Rule', {
      schedule: events.Schedule.cron({ minute: '0', hour: '7' })
    })
    
    rule.addTarget(new targets.LambdaFunction(evfunc))

    new CfnOutput(this, 'S3Output', { value: bucket.bucketName, description: "S3 bucket name" })
    new CfnOutput(this, 'LambdaOut', { value: func.functionName, description: "lambda function name" })
    new CfnOutput(this, 'LambdaEvOut', { value: evfunc.functionName, description: "lambda function name" })
    new CfnOutput(this, 'RuleOut', { value: rule.ruleName, description: "Eventbridge rule name" })
  }
}