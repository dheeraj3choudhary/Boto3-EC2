###Author - Dheeraj Choudhary
import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('employee')


resp = table.delete_item(
    Key={
        'id': 3
    }
)
