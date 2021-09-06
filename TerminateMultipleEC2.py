import boto3

client=boto3.client('ec2')

resp=client.describe_instances()

newlist=[]

for reservation in resp['Reservations']:
    for instance in reservation['Instances']:
            newlist.append(instance['InstanceId'])

print(newlist)
print(client.terminate_instances(InstanceIds=(newlist)))