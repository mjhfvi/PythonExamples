'''

'''


import boto3
ids = ['i-0dbb4d067f97816a6']
ec2 = boto3.resource('ec2')
ec2.instances.filter(InstanceIds = ids).stop()                  #for stopping an ec2 instance

# ec2.instances.filter(InstanceIds = ids).terminate()             #for terminating an ec2 instance


ids = ['i-0dbb4d067f97816a6']
ec2 = boto3.resource('ec2')
ec2.instances.filter(InstanceIds = ids).start()                  #for stopping an ec2 instance