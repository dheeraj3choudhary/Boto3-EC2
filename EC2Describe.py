import boto3

client = boto3.client('ec2')

resp = client.describe_instances()

for reservation in resp['Reservations']:
    for instance in reservation['Instances']:
        print("Running Instance Image ID: {} Running instance Instance Type: {} Running Instance Keyname {}"
              .format(instance['InstanceId'],instance['InstanceType'],instance['KeyName']))