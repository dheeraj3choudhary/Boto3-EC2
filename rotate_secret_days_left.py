# @Author:- Dheeraj Choudhary
import boto3
from datetime import datetime
from datetime import timedelta
from dateutil.tz import tzlocal
client = boto3.client('secretsmanager')

list_sec = client.list_secrets()
for i in list_sec['SecretList']:
    rotation_status = (i['RotationEnabled']) if 'RotationEnabled' in i else 'False'
    rotation_date = ('LastRotatedDate' in i)
    rotation_date = str(rotation_date)
    print(f"rotation_status = {rotation_status}{type(rotation_status)} And rotation_date = {rotation_date}{type(rotation_date)}")
    if (rotation_status == 'True') & (rotation_date == 'True'):
        response = client.describe_secret(SecretId=i['ARN'])
        #LastChangedDate = response['LastChangedDate']
        Last_Rotated = response['LastRotatedDate']
        AutomaticallyAfterDays = response['RotationRules']['AutomaticallyAfterDays']
        total = Last_Rotated + timedelta(days=AutomaticallyAfterDays)
        current_timestamp = datetime.now(tzlocal())
        days_left = total - current_timestamp
        if days_left.days <= 15:
            print(f"Days left for secret name '{response['Name']}' to be rotated = {days_left.days}")

