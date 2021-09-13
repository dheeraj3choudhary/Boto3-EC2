from datetime import datetime, timedelta, timezone
import boto3

ec2 = boto3.resource('ec2')

#Create a filter variable to store tags
tagfilters=[
    {
       'Name': 'tag:Env',
       'Values':['Production']
    }
]

snapshots=ec2.snapshots.filter(Filters=tagfilters)

for snapshot in snapshots:
    create_time=snapshot.start_time
    delete_time=datetime.now(tz=timezone.utc) - timedelta(days=10)
    if delete_time > create_time:
        print('Create time of snapshot is {} And Delete time of snapshot is {}'.
              format(create_time,delete_time))
        snapshot.delete()
        print('{} has been deleted'.format(snapshot.snapshot_id))
    else:
        print('Existing Snapshot {} is not less that 10 days old'.format(snapshot.snapshot_id))


