'''
Manage Amazon Instances

'''
import os
import paramiko,boto3
from time import sleep


ec2ID = boto3.resource('ec2')
ec2Client = boto3.client('ec2')

inputInstancesList = []
inputRemoteLocal = []

ip_address = "18.194.1.127"
port = 22
username = "tzahi"
password = "1a2b3c4d"

commandVersion = "lsb_release -a"
commandHostName = "hostname -I"
commandUpdate = "apt-get update && apt-get upgrade"
commandLs = "ls"
commandVersion = "lsb_release -a"
commandIP = "hostname"
instance_id = 'i-044f46ca1d9501a03'

print("\n*****  Welcome to Amazon Menu  *****")
def Menu():
    while (True):
        choice = input("\n***  Select from the List  *** \n"
                       "1. list All Available Instances in AWS\n"
                       "2. Show Running Instances in AWS\n"
                       "3. Stop Instances in AWS\n"
                       "4. Start Instances in AWS\n"
                       "5. Create Instances in AWS\n"
                       "6. Remove Instances in AWS\n"
                       "7. Run Remote Commands\n"
                       "8. --Exit--\n\n")

        if choice == "1":  ### list EC2 instance
            response = ec2Client.describe_instances()
            for reservation in response["Reservations"]:
                for instance in reservation["Instances"]:
                    print('\n####################  Start List  #########################\n')
                    print('Full Instances Information\n', instance)
                    print('\n\nInstances ID Numebr:\n', instance["InstanceId"])
                    print('\n\n##################  End List  #########################\n')
                    sleep(4)

        if choice == "2":  ### Status EC2 instance
            instances = ec2ID.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
            for instance in instances:
                print('\n####################  Start List  #########################\n')
                print('instance Name')
                print(instance.id, instance.instance_type)
            for status in ec2ID.meta.client.describe_instance_status()['InstanceStatuses']:
                print('\nInstance Status')
                print('\n', status)
                print('\n\n##################  End List  ###########################\n')
                sleep(4)

        if choice == "3":                                           ### Start EC2 instance
            InstanceIdStop = input('Enter the InstanceID You Want to Stop:  ')
            ec2ID.instances.filter(InstanceIds=[InstanceIdStop]).stop()
            sleep(4)

        if choice == "4":                                           ### Start EC2 instance
            InstanceIdStart = input('Enter the InstanceID You Want to Start:  ')
            ec2ID.instances.filter(InstanceIds=[InstanceIdStart]).start()
            sleep(4)

        if choice == "5":                                           ### Create new EC2 instance
            CreateInstance = int(input("Enter Amount of Instance to Create (Image type Amazon Linux AMI 2018.03.0): "))
            instances = ec2ID.create_instances(
                ImageId='ami-0ace5544897bcc140',                                ### Image type Amazon Linux AMI 2018.03.0 (HVM), SSD Volume Type
                MinCount=CreateInstance,
                MaxCount=CreateInstance,
                InstanceType='t2.micro',
                KeyName='KEY_PAIR_NAME')
            sleep(4)

        if choice == "6":                                                       ### Remove new EC2 instance
            TerminateID = [input("Enter ID to Terminate:  ")]
            ec2ID.instances.filter(InstanceIds=TerminateID).terminate()
            sleep(4)

        if choice == "7":                                                       ### Remove new EC2 instance
            print("\n*****  Run Remote Command Menu  *****")
            def Menu2():
                while (True):
                    choice = input("\n***  Select from the List  ***\n"
                                   "1. List All Amazon Computers\n"
                                   "2. Add Computer to Work on\n"
                                   "3. Get OS Version\n"
                                   "4. Get Computer Hostname\n"
                                   "5. Run System Update\n"
                                   "6. Install AwsCli Tool\n"
                                   "7. Install Nagios Client\n"
                                   "8. Print TEST\n"
                                   "9. --Go Back--\n\n")
                    if choice == "1":
                        response = ec2Client.describe_instances()
                        for reservation in response["Reservations"]:
                            for instance in reservation["Instances"]:
                                print('\n####################  Start List  #########################\n')
                                print('Full Instances Information\n', instance)
                                print('\n\nInstances ID Numebr:\n', instance["InstanceId"])
                                print('\n\n##################  End List  #########################\n')
                        sleep(4)
                        continue
                    if choice == "2":
                        inputInstancesList = input('Enter the InstanceID or IP Address:  ')
                        while True:
                            inputRemoteLocal = input('is it a remote or local machine?  select R/L:   ')
                            if inputRemoteLocal == 'r':
                                print('you selected a Remote Machine')
                                return
                            if inputRemoteLocal == 'l':
                                print('you selected a local Machine')
                                return
                            else:
                                print('\n*** only select R for remote and L for local ***')
                                continue
                        sleep(4)
                    if choice == "3":
                        if inputRemoteLocal == 'l':
                            ssh = paramiko.SSHClient()
                            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                            ssh.connect(inputInstancesList, port, username, password)
                            stdin, stdout, stderr = ssh.exec_command(commandVersion)
                            lines = stdout.readlines()
                            if any("Ubuntu" in s for s in lines):
                                print('This is an Ubuntu Machine')
                            if any("CentOS" in s for s in lines):
                                print('This is an CentOS Machine')
                        if inputRemoteLocal == 'r':
                            ssh = paramiko.SSHClient()
                            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                            ssh.connect(inputInstancesList, port, username, password)
                            stdin, stdout, stderr = ssh.exec_command(commandVersion)
                            lines = stdout.readlines()
                            sleep(4)
                            continue
                    if choice == "4":
                        if inputRemoteLocal == 'r':
                            def ssh_connect_with_retry(ssh, ip_address, retries):
                                if retries > 3:
                                    return False
                                privkey = paramiko.RSAKey.from_private_key_file('/tmp/TzahiCohenKey.pem')
                                interval = 5
                                try:
                                    retries += 1
                                    print('SSH into the instance: {}'.format(ip_address))
                                    ssh.connect(hostname=ip_address,
                                                username='ec2-user', pkey=privkey)
                                    return True
                                except Exception as e:
                                    print(e)
                                    time.sleep(interval)
                                    print('Retrying SSH connection to {}'.format(ip_address))
                                    ssh_connect_with_retry(ssh, ip_address, retries)
                                    # get instance
                                    ec2 = boto3.resource('ec2', region_name='eu-central-1')
                                    instance = ec2.Instance(id=instance_id)
                                    instance.wait_until_running()
                                    current_instance = list(ec2.instances.filter(InstanceIds=[instance_id]))
                                    ip_address = current_instance[0].public_ip_address
                                    ssh = paramiko.SSHClient()
                                    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                                    ssh_connect_with_retry(ssh, ip_address, 0)
                                    stdin, stdout, stderr = ssh.exec_command('hostname')
                                    print('stdout:', stdout.read())
                                    print('stderr:', stderr.read())
                        if inputRemoteLocal == 'l':
                            ssh = paramiko.SSHClient()
                            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                            ssh.connect(inputInstancesList, port, username, password)
                            stdin, stdout, stderr = ssh.exec_command(commandUpdate)
                            lines = stdout.readlines()
                            print(lines)
                            sleep(4)
                            continue
                    if choice == "5":
                        ssh = paramiko.SSHClient()
                        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        ssh.connect(inputInstancesList, port, username, password)
                        stdin, stdout, stderr = ssh.exec_command(commandUpdate)
                        lines = stdout.readlines()
                        print(lines)
                        sleep(4)
                        continue
                    if choice == "6":
                        continue
                    if choice == "7":
                        continue
                    if choice == "8":
                        print(inputInstancesList)
                        continue
                    if choice == "9":
                        break
            Menu2()

        if choice == "8":
            choiceYN = input("Are You Sure? Y/N \n").lower()
            if choiceYN == "y":
                print("Exiting the System...")
                sleep(2)
                break

            if choiceYN == "n":
                print("Welcome Back......")
                sleep(2)
                continue

Menu()
