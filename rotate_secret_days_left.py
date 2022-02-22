# @Author:- Dheeraj Choudhary
import boto3
import pprint
from datetime import datetime
from datetime import timedelta
from dateutil.tz import tzlocal

client = boto3.client('secretsmanager')
list_sec = client.list_secrets()
for i in list_sec['SecretList']:
    rotation_status = 'RotationEnabled' in i
    #check = 'LastRotatedDate' in i
    if rotation_status:
        response = client.describe_secret(SecretId=i['ARN'])
        LastChangedDate = response['LastChangedDate']
        AutomaticallyAfterDays = response['RotationRules']['AutomaticallyAfterDays']
        total = LastChangedDate + timedelta(days=AutomaticallyAfterDays)
        current_timestamp = datetime.now(tzlocal())
        days_left = total - current_timestamp
        print(f"Days left for secret name '{response['Name']}' to be rotated = {days_left.days}")



