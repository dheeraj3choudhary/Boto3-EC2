import boto3

client = boto3.client('s3')

bucket_name=str(input('Please input bucket name to be created: '))

#Bucket Name argument is mandatory and bucket name should be unique
response1 = client.create_bucket(
    ACL='private',
    Bucket=bucket_name
    )

print(response1['Location'])

tag_resp=str(input('Press "y" if you want to tag your bucket?: '))

if tag_resp == 'y':
    tag_key=str(input("Please enter key for the tag: "))
    tag_value = str(input("Please enter value for the tag: "))
    response2 = client.put_bucket_tagging(
    Bucket=bucket_name,
    Tagging={
        'TagSet': [
            {
                'Key': tag_key,
                'Value': tag_value
            }
        ]
    })
