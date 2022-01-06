###Author - Dheeraj Choudhary
import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('employee')

resp = table.update_item(
    Key={'id': 1},
    UpdateExpression="SET salary= :s",
    ExpressionAttributeValues={':s': 20},
    ReturnValues="UPDATED_NEW"
)
print(resp['Attributes'])
