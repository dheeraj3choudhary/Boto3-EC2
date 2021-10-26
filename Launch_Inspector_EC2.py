import boto3

client = boto3.client('ec2')

# Script to install AWS Inspector agent on EC2 
user_data = '''#!/bin/bash
sudo wget https://inspector-agent.amazonaws.com/linux/latest/install
sudo curl -O https://inspector-agent.amazonaws.com/linux/latest/install
sudo bash install'''

# Create a security group and allow SSH inbound rule through the VPC
security_resp = client.create_security_group(GroupName='Inspector-SG',
                                             Description='Security group for aws Inspector',
                                             VpcId='<Your VPC ID>')
security_group_id = security_resp['GroupId']
print(security_group_id)

sgrule_ingress = client.authorize_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[
            {'IpProtocol': 'tcp',
             'FromPort': 20,
             'ToPort': 20,
             'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
            {'IpProtocol': 'tcp',
             'FromPort': 21,
             'ToPort': 21,
             'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
            {'IpProtocol': 'tcp',
             'FromPort': 23,
             'ToPort': 23,
             'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}

        ])

resp = client.run_instances(ImageId='ami-0742b4e673072066f',
                          InstanceType='t2.micro',
                          MinCount=2,
                          MaxCount=2,
                          KeyName=<Your KeyName>,
                          UserData=user_data,
                          SecurityGroups=['Inspector-SG'],
                          TagSpecifications=[
                              {
                                  'ResourceType': 'instance',
                                  'Tags': [{'Key': 'Name','Value': 'EC2-Inspector'},]
                              },
                          ],
                          )
for i in resp['Instances']:
    print("Instance ID Created is :{} Instance Type Created is : {}" .format(i['InstanceId'],i['InstanceType']))
