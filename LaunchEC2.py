import boto3

client = boto3.client('ec2')

#Please select image id as per your EC2 instance requirement.
resp=client.run_instances(ImageId='<Image ID>',
                          InstanceType='t2.micro',
                          MinCount=1,
                          MaxCount=1,
                          KeyName='<keyname>') #Enter your key name here
for i in resp['Instances']:
    print("Instance ID Created is :{} Instance Type Created is : {}" .format(i['InstanceId'],i['InstanceType']))
