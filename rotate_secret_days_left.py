# @Author:- Dheeraj Choudhary
import boto3
import pprint
from datetime import datetime
from datetime import timedelta
from dateutil.tz import tzlocal
client = boto3.client('secretsmanager')
response = client.describe_secret(
    SecretId='<Secret ARN>'
)
#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(response)
#print("Days left to be rotated = {}".format(response['RotationRules']['AutomaticallyAfterDays']))
#print(response['LastChangedDate'])
LastChangedDate = response['LastChangedDate']
AutomaticallyAfterDays = response['RotationRules']['AutomaticallyAfterDays']
total = LastChangedDate + timedelta(days=AutomaticallyAfterDays)
print(LastChangedDate)
print(total)
'''
import pytz
UTC = pytz.utc
IST = pytz.timezone('Asia/Kolkata')
datetime.now(IST)
'''
current_timestamp = datetime.now(tzlocal())
days_left = total - current_timestamp
print(days_left.days)



