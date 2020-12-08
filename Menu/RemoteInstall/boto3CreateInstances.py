'''
source: https://blog.ipswitch.com/how-to-create-an-ec2-instance-with-python

'''

import boto3
ec2 = boto3.resource('ec2')

# create a new EC2 instance
instances = ec2.create_instances(
     ImageId='ami-0a07be880014c7b8e',
     MinCount=1,
     MaxCount=2,
     InstanceType='t2.micro',
     KeyName='ec2-keypair'
 )