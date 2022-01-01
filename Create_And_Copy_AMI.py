import boto3

ec2 = boto3.resource('ec2', region_name='us-east-1')
image_ids = []

instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

for instance in instances:
    print(instance.id,instance.placement)
    image = instance.create_image(Name='AMI Copy For '+instance.id)
    image_ids.append(image.id)

print("Images to be copied are ", image_ids)

# Waiting For Images Using Paginators

ec2_client = boto3.client('ec2', region_name='us-east-1')
waiter = ec2_client.get_waiter('image_available')
waiter.wait(Filters=[{
 'Name': 'image-id',
 'Values': image_ids
}])

# Copy Images To Other Regions

ec2_client = boto3.client('ec2', region_name='us-west-1')
for image_id in image_ids:
    ec2_client.copy_image(Name='AMI Copy From US-EAST-1'+image_id, SourceImageId=image_id, SourceRegion='us-east-1')
