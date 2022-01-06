###Author - Dheeraj Choudhary
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employee')
table.delete()
