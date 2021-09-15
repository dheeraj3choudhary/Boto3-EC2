import boto3

client = boto3.client('s3')

bucket_name=str(input('Please input bucket name to be deleted: '))

print("Before deleting the bucket we need to check if its empty. Cheking ...")

objs = client.list_objects_v2(Bucket=bucket_name)
fileCount = objs['KeyCount']

if fileCount == 0:
    response = client.delete_bucket(Bucket=bucket_name)
    print("{} has been deleted successfully !!!".format(bucket_name))
else:
    print("{} is not empty {} objects present".format(bucket_name,fileCount))
    print("Please make sure S3 bucket is empty before deleting it !!!")
