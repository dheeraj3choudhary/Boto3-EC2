###Author - Dheeraj Choudhary
import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('employee')
table.put_item(
    Item={
        'id': 1,
        'name': 'ABC',
        'salary': 20000
    },
)
table.put_item(
    Item={
        'id': 2,
        'name': 'DEF',
        'salary': 22000
    },
)
table.put_item(
    Item={
        'id': 3,
        'name': 'XYZ',
        'salary': 25000
    },
)
