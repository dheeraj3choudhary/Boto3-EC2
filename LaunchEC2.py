import boto3

client = boto3.client('ec2')

resp=client.run_instances(ImageId='ami-0742b4e673072066f',
                          InstanceType='t2.micro',
                          MinCount=1,
                          MaxCount=1,
                          KeyName='CustomVPC')
for i in resp['Instances']:
    print("Instance ID Created is :{} Instance Type Created is : {}" .format(i['InstanceId'],i['InstanceType']))
