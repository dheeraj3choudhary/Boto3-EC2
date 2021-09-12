import boto3

client = boto3.client('ec2')


#Make sure to add values in '<>' for Image ID and Key name as per your requirement
resp1=client.run_instances(ImageId='<Image ID>',
                          InstanceType='t2.micro',
                          MinCount=1,
                          MaxCount=1,
                          KeyName='<Your Key Name>',
                          TagSpecifications=[
                              {
                                  'ResourceType': 'instance',
                                  'Tags': [{'Key': 'Env','Value': 'Production'},]
                              },
                          ],
                          )
#Make sure to add values in '<>' for Image ID and Key name as per your requirement
resp2=client.run_instances(ImageId='<Image ID>',
                          InstanceType='t2.micro',
                          MinCount=1,
                          MaxCount=1,
                          KeyName='<Your Key Name>',
                          TagSpecifications=[
                              {
                                  'ResourceType': 'instance',
                                  'Tags': [{'Key': 'Env','Value': 'UAT'},]
                              },
                          ],
                          )
for i in resp1['Instances']:
    print("Instance ID Created is :{} Instance Type Created is : {}" .format(i['InstanceId'],i['InstanceType']))
    
for i in resp2['Instances']:
    print("Instance ID Created is :{} Instance Type Created is : {}" .format(i['InstanceId'],i['InstanceType']))
