import boto3

ec2 = boto3.resource('ec2')

#Create a filter variable
tagfilters=[
    {
       'Name': 'tag:Env',
       'Values':['Production']
    }
]

for instance in ec2.instances.filter(Filters=tagfilters):
    for volume in instance.volumes.all():
        snapshot=volume.create_snapshot(Description='Snapshot created via script',
                                        TagSpecifications=[
                                            {
                                                'ResourceType': 'snapshot',
                                                'Tags': [{'Key': 'Env', 'Value': 'Production'}, ]
                                            },
                                        ],
                                        )
