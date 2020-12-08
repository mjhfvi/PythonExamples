'''
Manage Amazon

'''
import os
import boto3
from time import sleep

InstanceID = ['i-0dbb4d067f97816a6']
ec2ID = boto3.resource('ec2')
ec2Client = boto3.client('ec2')

print("\n*****  Welcome to Amazon Menu  *****")
def Menu():
    while (True):
        choice = input("\n***  Select from the List  *** \n"
                       "1. list Instances\n"
                       "2. Status Instances\n"
                       "3. Stop Instances\n"
                       "4. Start Instances\n"
                       "5. Create Instances\n"
                       "6. Remove Instances\n"
                       "7. --Exit--\n\n")

        if choice == "1":
            response = ec2Client.describe_instances()
            for reservation in response["Reservations"]:
                for instance in reservation["Instances"]:
                    print(instance)
                    print(instance["InstanceId"])
            sleep(4)
            os.system('cls')

        if choice == "2":                                           ### Status EC2 instance
            instances = ec2ID.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
            for instance in instances:
                print(instance.id, instance.instance_type)
            for status in ec2ID.meta.client.describe_instance_status()['InstanceStatuses']:
                print(status)

        if choice == "3":                                           ### Start EC2 instance
            ec2ID.instances.filter(InstanceIds=InstanceID).stop()
            sleep(4)
            os.system('cls')

        if choice == "4":                                           ### Start EC2 instance
            ec2ID.instances.filter(InstanceIds=InstanceID).start()
            sleep(4)
            os.system('cls')

        if choice == "5":                                           ### Create new EC2 instance
            # inputImageID = [input("Enter Image ID:   ")]
            # inputMinCount = [input("Enter Min Count:   ")]
            # inputMaxCount = [input("Enter Max Count:   ")]
            instances = ec2ID.create_instances(
                ImageId='ami-0a07be880014c7b8e',
                MinCount=1,
                MaxCount=2,
                InstanceType='t2.micro',
                KeyName='ec2-keypair')
            sleep(4)
            os.system('cls')

        if choice == "6":                                           ### Remove new EC2 instance
            TerminateID = [input("Enter ID to Terminate:  ")]
            ec2ID.instances.filter(InstanceIds=TerminateID).terminate()
            sleep(4)
            os.system('cls')

        if choice == "7":
            choiceYN = input("Are You Sure? Y/N \n").lower()
            if choiceYN == "y":
                os.system('cls')
                print("Exiting the System...")
                sleep(2)
                os.system('cls')
                break

            if choiceYN == "n":
                print("Welcome Back......")
                sleep(2)
                os.system('cls')
                continue

Menu()
