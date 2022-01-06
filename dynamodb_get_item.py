###Author - Dheeraj Choudhary
import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('employee')

resp = table.get_item(
    Key={
        'id': 1
    },
)
print(resp['Item'])
