### Author:-Dheeraj Choudhary
import boto3
ec2 = boto3.client('ec2')
response = ec2.create_volume(
    AvailabilityZone='us-east-1a',
    Size=20,
    VolumeType='gp2',
    TagSpecifications=[
        {
            'ResourceType': 'volume',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Unused_Vol1'
                },
            ]
        },
    ],
)
