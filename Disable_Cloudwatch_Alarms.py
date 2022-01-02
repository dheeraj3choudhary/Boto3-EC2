###Author :- Dheeraj Choudhary

import boto3
client = boto3.client('cloudwatch')

response = client.describe_alarms()
#names = [[alarm['AlarmName'] for alarm in response['MetricAlarms']]]

for alarm in response['MetricAlarms']:
    status = alarm['ActionsEnabled']
    if status:
        name = alarm['AlarmName']
        print(name)
        disable_alarm = client.disable_alarm_actions(AlarmNames=[name])
        print("Alarm {} is disabled".format(name))
        file1 = open("D:\Python Impetus\AWS_Boto3\myfile.txt", "a")
        file1.write(name+"\n")
    else:
        print("No enabled Alarms")
