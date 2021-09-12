import boto3

ec2 = boto3.resource('ec2')

#Create a filter variable
tagfilters=[
    {
       'Name': 'tag:Env',
       'Values':['Production']
    },
    {
       'Name': 'tag:Env',
       'Values':['UAT']
    }
]

snapshot_list=[] #Empty list which we will require to store our list of snapshot_ids

for instance in ec2.instances.filter(Filters=tagfilters):
    for volume in instance.volumes.all():
        snapshot=volume.create_snapshot(Description='Snapshot created via script')
        snapshot_list.append(snapshot.snapshot_id)

print(snapshot_list)

sns_client.publish(
    TopicArn='<SNS Topic ARN>',
    Subject='EBS Snapshots',
    Message=str(snapshot_list)
)
