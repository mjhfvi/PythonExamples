import os
import boto3
from time import sleep

InstanceID = ['i-0dbb4d067f97816a6']
ec2ID = boto3.resource('ec2')
# ec2 = boto3.resource('ec2')
# ids = ['i-0dbb4d067f97816a6']



# ec2ID.create_instances(ImageId=InstanceID, MinCount=1, MaxCount=5)                                        ### create new instances
ec2ID.instances.filter(InstanceIds=InstanceID).start()                                                    ### start instances
# ec2ID.instances.filter(InstanceIds=InstanceID).stop()                                                     ### stop instances

instances = ec2ID.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])      ### Checking if instances are running
for instance in instances:
    print(instance.id, instance.instance_type)

for status in ec2ID.meta.client.describe_instance_status()['InstanceStatuses']:                            ### status  instances
    print(status)