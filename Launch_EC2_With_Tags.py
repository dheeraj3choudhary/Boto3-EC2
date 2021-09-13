import boto3

client = boto3.client('ec2')

resp=client.run_instances(ImageId='<Image ID>',
                          InstanceType='t2.micro',
                          MinCount=1,
                          MaxCount=1,
                          KeyName='<Key Name>',
                          TagSpecifications=[
                              {
                                  'ResourceType': 'instance',
                                  'Tags': [{'Key': 'Name','Value': 'Linux Server'},
                                           {'Key': 'Env','Value': 'Production'}]
                              },
                          ],
                          )
for i in resp['Instances']:
    print("Instance ID Created is :{} Instance Type Created is : {}" .format(i['InstanceId'],i['InstanceType']))
