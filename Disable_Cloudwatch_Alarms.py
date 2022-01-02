###Author :- Dheeraj Choudhary

import boto3
client = boto3.client('cloudwatch')

response = client.describe_alarms()

for alarm in response['MetricAlarms']:
    status = alarm['ActionsEnabled']
    if status:
        name = alarm['AlarmName']
        disable_alarm = client.disable_alarm_actions(AlarmNames=[name])
        print("Alarm {} is disabled".format(name))
        file1 = open("myfile.txt", "a")
        file1.write(name+"\n")
    else:
        print("No enabled Alarms")
