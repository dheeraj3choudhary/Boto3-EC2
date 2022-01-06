###Author - Dheeraj Choudhary
import boto3

dynamodb = boto3.resource('dynamodb')

response = dynamodb.batch_get_item(
        RequestItems={
            'employee': {
                'Keys': [
                    {
                        'id': 1
                    },
                    {
                        'id': 2
                    },
                ],
                'ConsistentRead': True
            }
        },
        ReturnConsumedCapacity='TOTAL'
    )
print(response['Responses'])
