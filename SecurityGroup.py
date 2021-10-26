import boto3

client = boto3.client('ec2')

# Create a security group and allow SSH inbound rule through the VPC
security_resp = client.create_security_group(GroupName='<Security group name>',
                                             Description='Security group for aws Inspector',
                                             VpcId='<Your VPC ID>')
security_group_id = security_resp['GroupId']
print(security_group_id)

sgrule_ingress = client.authorize_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[
            {'IpProtocol': 'tcp',
             'FromPort': 22,
             'ToPort': 22,
             'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
            {'IpProtocol': 'tcp',
             'FromPort': 20,
             'ToPort': 20,
             'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
            {'IpProtocol': 'tcp',
             'FromPort': 21,
             'ToPort': 21,
             'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
            {'IpProtocol': 'tcp',
             'FromPort': 23,
             'ToPort': 23,
             'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}

        ])
