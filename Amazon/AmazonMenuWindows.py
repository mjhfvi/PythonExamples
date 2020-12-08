'''
Manage VM`s in Amazon and VirtualBox
Windows - Change pem key permissions, https://superuser.com/questions/1296024/windows-ssh-permissions-for-private-key-are-too-open
'''

import paramiko
import boto3
import os
import subprocess
import json
from time import sleep

######################  File Info  ####################################################
win_file_name = "D:\\LocalComputerList.json"
win_access_key = "D:\\Amazon\\Key.pem"

lin_file_name = "/tmp/LocalComputerList.json"
lin_access_key = "/tmp/Amazon/TzahiCohenKey.pem"

############  Testing for an Existing Orders.json File  ###############################
try:
    open(lin_file_name)
except IOError:
    # FileComputerList = open(file_name, "w+")
    with open(lin_file_name, 'w') as json_file:
        json.dumps()
        # jsonFile.write('\n')
        json_file.close()
    print("Successfully created the file %s " % lin_file_name)
# else:
# print("File %s Exists" % fileName)

############  Amazon Configuration  ####################################################
ec2ID = boto3.resource('ec2')
ec2Client = boto3.client('ec2')

############  VM Commands  #############################################################
command_ls = "ls"
command_version = "hostnamectl"
command_ubuntu_os_update = "apt-get update && apt-get upgrade"
command_cent_os_update = "yum check-update && yum update"
command_ubuntu_insatll_awscli = "apt-get install awscli"
command_cent_insatll_awscli = "pip3 install awscli"
command_insatll_python = "pip3 install python3 python3-pip"
command_ip_addr = "ip addr"
command_docker_list = "docker ps -a"
command_docker_start_container = "docker container start "
command_docker_stop_container = "docker container stop "
command_docker_remove_container = "docker container rm "
command_docker_new_container = "docker run -d "
command_docker_list_container = "docker container ls -a"
command_docker_list_image = "docker image ls"
command_docker_pull_image = "docker image pull "
command_docker_remove_image = "docker image rm "
command_docker_run = 'docker run -d '
command_docker_port = '-p '
command_docker_name = '--name '
# command_virtualbox_list = ["C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe", 'list', 'vms']
# command_virtualbox_list_running = ["C:\\'Program Files'\\Oracle\\VirtualBox\\vboxmanage", 'list', 'runningvms']
# command_virtualbox_list_ostypes = ["C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe", 'list', 'ostypes']
# command_open_puttygen = ["C:\\Program Files\\PuTTY\\puttygen.exe"]


############  Menu Information  ##########################

def main_menu():
    print("\n        *****  Main Menu  *****")
    while True:
        choice = input("\n1. Enter A Computer Name or IP Address\n"
                       "2. Setup New Environment, Install Software       (Linux Only) [Locally]"
                       "3. "
                       "4. Quick Access - List All VM`s in VirtualBox  (Windows Only) [Locally]\n"
                       "5. Quick Access - List All VM`s in Docker                     [Locally]\n"
                       "6. Quick Access - List All VM`s in AWS                        [Remotely]\n"
                       "7. Configuration Menu\n"
                       " --------------------------------------------\n"
                       "9.  --- EXIT ---\n")
        if choice == "1":
            ip_input = input('IP Address: ')
            # if ip_input in json_data:
            #     print('IP Address is in the list..')
            # else:
            #     print('we don`t have that IP in out list!')

        if choice == "4":
            subprocess.call(command_virtualbox_list)
            continue

        if choice == "5":
            subprocess.call(command_docker_list)
            continue

        if choice == "6":
            response = ec2Client.describe_instances()
            for reservation in response["Reservations"]:
                for instance in reservation["Instances"]:
                    print('Full Instances Information\n', instance)
                    print('\n\nInstances ID Number:\n', instance["InstanceId"])
            continue

        if choice == "7":
            configuration_menu()
            continue

        if choice == "9":
            choiceYN = input("Are You Sure? Y/N \n").lower()
            if choiceYN == "y":
                print("Exiting the System...")
                sleep(2)
                break

            if choiceYN == "n":
                print("Welcome Back......")
                sleep(2)
                continue

    # else:
    #     print('Only Select the Options on the Menu!')

def configuration_menu():
    while True:
        choice = input('\n  ***  Configuration Menu  ***\n'
                       '1. VirtualBox Menu\n'
                       '2. Docker Menu\n'
                       '3. AWS Menu\n'
                       '4. List local File\n'
                       '5. \n'
                       '6. \n'
                       '7. Open PuTTYgen to generate an SSH key (Windows Only)\n'
                       '9.  --- Back to Main Menu ----\n')
        if choice == "1":
            virtualbox_start_menu()
            continue

        if choice == "2":
            docker_start_menu()
            continue

        if choice == "3":
            amazon_start_menu()
            continue

        if choice == "4":
            continue

        if choice == "5":
            continue

        if choice == "6":
            continue

        if choice == "7":
            subprocess.call(command_open_puttygen)
            continue

        if choice == "9":
            break

        else:
            print('Only Select the Options on the Menu!')

def virtualbox_start_menu():
    while True:
        choice = input("\n*****  VirtualBox Start Menu (Windows Only) *****\n"
                       "1. Command Menu\n"
                       "2. Instances Menu\n"
                       "---------------------\n"
                       "9. Back to Start Menu \n\n")
        if choice == "1":
            virtualbox_command_menu()
            continue

        if choice == "2":
            virtualbox_instances_menu()
            continue

        if choice == "9":
            break

def virtualbox_instances_menu():
    while True:
        choice = input("\n*****  VirtualBox Instances Menu (Windows Only) *****\n"
                       "1. List All VM`s\n"
                       "2. List All Running VM`s\n"
                       "3. List All OS Types VM`s\n"
                       "4. Start VM\n"
                       "5. Stop VM\n"
                       "---------------------\n"
                       "9. Back to VirtualBox Start Menu \n\n")
        if choice == "1":
            subprocess.call(command_virtualbox_list)
            continue

        if choice == "2":
            subprocess.call(command_virtualbox_list_running)
            continue

        if choice == "3":
            subprocess.call(command_virtualbox_list_ostypes)
            continue

        if choice == "3":
            input_virtualbox_name = input("Enter VirtualBox VM Name: ")
            # vm_name = [input_virtualbox_name]
            # command_virtualbox_start_vm = ["C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe", 'startvm', input_virtualbox_name]
            # subprocess.call("C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe", 'startvm', 'vm_name')
            continue


        if choice == "9":
            break

def virtualbox_command_menu():
    while True:
        choice = input("\n*****  VirtualBox Command Menu (Windows Only) *****\n"
                       "1. Enter IP Address to Work on\n"
                       "2. Get OS Version\n"
                       "3. Get Computer Hostname\n"
                       "4. Run System Update\n"
                       "5. Install AwsCli Tool\n"
                       "6. Print IP Address\n"
                       "---------------------\n"
                       "9. Back to Start Menu \n\n")
        if choice == "1":
            input_instances_ip = input("Enter the InstanceID or IP Address:  ")
            continue

        if choice == "2":
            computer_host = paramiko_connection(input_instances_ip)
            if any("Ubuntu" in s for s in computer_host):
                print('This is an Ubuntu Machine')
            if any("CentOS" in s for s in computer_host):
                print('This is an CentOS Machine')
                sleep(2)
                continue

        if choice == "3":
            computer_host = paramiko_connection(input_instances_ip)
            if any("Ubuntu" in s for s in computer_host):
                print('This is an Ubuntu Machine')
            if any("CentOS" in s for s in computer_host):
                print('This is an CentOS Machine')
                sleep(2)
                continue

        if choice == "4":
            computer_host = paramiko_connection(input_instances_ip)
            if any("Ubuntu" in s for s in computer_host):
                print('This is an Ubuntu Machine, running the apt-get command ')
                stdin, stdout, stderr = ssh.exec_command(command_ubuntu_os_update)
            if any("CentOS" in s for s in computer_host):
                print('This is an CentOS Machine, running the yum command ')
                stdin, stdout, stderr = ssh.exec_command(command_cent_os_update)
                sleep(2)
                continue

        if choice == "5":
            computer_host = paramiko_connection(input_instances_ip)
            if any("Ubuntu" in s for s in computer_host):
                print('This is an Ubuntu Machine, running the apt-get install awscli command ')
                stdin, stdout, stderr = ssh.exec_command(command_ubuntu_insatll_awscli)
            if any("CentOS" in s for s in computer_host):
                print('This is an CentOS Machine, running the pip3 install awscli command ')
                stdin, stdout, stderr = ssh.exec_command(command_cent_insatll_awscli)
                sleep(2)
                continue

        if choice == "6":
            computer_host = paramiko_connection(input_instances_ip)
            if any("Ubuntu" in s for s in computer_host):
                print('This is an Ubuntu Machine, running the ip addr command ')
                stdin, stdout, stderr = ssh.exec_command(command_ip_addr)
                print("Local IP Address is")
            if any("CentOS" in s for s in computer_host):
                print('This is an CentOS Machine, running the ip addr command ')
                stdin, stdout, stderr = ssh.exec_command(command_ip_addr)
                print("Local IP Address is")
                sleep(2)
                continue

        if choice == "9":
            break
        break

def amazon_start_menu():
    while True:
        choice = input("\n*****  Amazon Menu  *****\n"
                       "1. Instances Menu\n"
                       "2. Command Menu\n"
                       "---------------------\n"
                       "9. Back to Start Menu \n\n")
        if choice == "1":
            amazon_instances_menu()
            continue

        if choice == "2":
            amazon_command_menu()
            continue

        if choice == "9":
            break
        break

def amazon_instances_menu():
    while True:
        choice = input("*****  Amazon Menu Instances  *****\n"
                       "1. Show Running Amazon Instances\n"
                       "2. Stop Amazon Instances\n"
                       "3. Start Amazon Instances\n"
                       "4. Create Amazon Instances\n"
                       "5. Remove Amazon Instances\n"
                       "---------------------\n"
                       "9. Back to Amazon Menu \n\n")
        if choice == "1":
            if not inputInstancesList:
                print("List is empty, Please add a Computer Name or IP Address")
                inputInstancesList = input("Enter the InstanceID or IP Address:  ")
            else:
                response = ec2Client.describe_instances()
                for reservation in response["Reservations"]:
                    for instance in reservation["Instances"]:
                        print('Full Instances Information\n', instance)
                        print('\n\nInstances ID Numebr:\n', instance["InstanceId"])
                        sleep(2)
                        os.system('cls')
                        continue

        if choice == "2":
            if not inputInstancesList:
                print("List is empty, Please add a Computer Name or IP Address")
                inputInstancesList = input("Enter the InstanceID or IP Address:  ")
            else:
                InstanceIdStop = input('Enter the InstanceID You Want to Stop:  ')
                ec2ID.instances.filter(InstanceIds=[InstanceIdStop]).stop()
                sleep(2)
                os.system('cls')
                continue

        if choice == "3":
            if not inputInstancesList:
                print("List is empty, Please add a Computer Name or IP Address")
                inputInstancesList = input("Enter the InstanceID or IP Address:  ")
            else:
                InstanceIdStop = input('Enter the InstanceID You Want to Start:  ')
                ec2ID.instances.filter(InstanceIds=[InstanceIdStop]).start()
                sleep(2)
                os.system('cls')
                continue

        if choice == "4":
            inputInstancesList = input("Enter the InstanceID or IP Address:  ")
            json_data = json_read()

            if not json_data:
                print("List is empty, Please add a Computer Name or IP Address")

            else:
                CreateInstance = int(input("Enter Amount of Instance to Create (Image type Amazon Linux AMI 2018.03.0): "))
                instances = ec2ID.create_instances(
                    ImageId='ami-0ace5544897bcc140',
                    ### Image type Amazon Linux AMI 2018.03.0 (HVM), SSD Volume Type
                    MinCount=CreateInstance,
                    MaxCount=CreateInstance,
                    InstanceType='t2.micro',
                    KeyName=access_key)
                sleep(2)
                os.system('cls')
                continue

        if choice == "5":
            if not inputInstancesList:
                print("List is empty, Please add a Computer Name or IP Address")
                inputInstancesList = input("Enter the InstanceID or IP Address:  ")
            else:
                TerminateID = [input("Enter ID to Terminate:  ")]
                ec2ID.instances.filter(InstanceIds=TerminateID).terminate()
                sleep(2)
                os.system('cls')
                continue

        if choice == "9":
            break

def amazon_command_menu():
    while True:
        choice = input("\n*****  Amazon Menu  *****\n"
                       "1. Get OS Version\n"
                       "2. Get Computer Hostname\n"
                       "3. Run System Update\n"
                       "4. Install AwsCli Tool\n"
                       "5. Print Public IP Address\n"
                       "---------------------\n"
                       "9. Back to Amazon Menu \n\n")
        if choice == "1":
            continue

        if choice == "2":
            continue

        if choice == "3":
            continue

        if choice == "4":
            continue

        if choice == "5":
            continue

        if choice == "6":
            continue

        if choice == "9":
            break
        break

def docker_start_menu():
    while True:
        choice = input("*****  Docker Menu Instances  *****\n"
                       "1. Show Running Docker Containers\n"
                       "2. Stop Docker Container\n"
                       "3. Start Docker Container\n"
                       "4. Create Docker Container\n"
                       "5. Remove Docker Container\n"
                       "6. Pull Image, [Ubuntu] [Centos]\n"
                       "7. Remove Image\n"
                       "---------------------\n"
                       "9. Back to Main Menu \n\n")
        if choice == "1":
            subprocess.call(command_docker_list)
            continue

        if choice == "2":
            docker_id = input('Enter the container ID:  ')
            subprocess.call(command_docker_stop_container + docker_id)
            continue

        if choice == "3":
            docker_id = input('Enter the container ID:  ')
            subprocess.call(command_docker_start_container + docker_id)
            continue

        if choice == "4":
            subprocess.call(command_docker_list_image)
            choice_container = input('How May Container to build? ')
            if choice_container == "1":
                input_image_name = input('Enter image ID:  ')
                input_container_name = input('Enter the Container Name:  ')
                docker_port_in = input('Enter the Container Internal Port:  ')
                docker_port_out = input('Enter the Container external Port:  ')
                subprocess.call(command_docker_run + command_docker_port + docker_port_in + ":" + docker_port_out + " " + command_docker_name + input_container_name + " " + input_image_name)
            else:
                input_image_name = input('Enter image ID:  ')
                input_container_name = input('Enter the Container Name:  ')
                # for i in [1..choice_container]
                #     subprocess.call(command_docker_run + command_docker_name + input_image_name)

            continue

        if choice == "5":
            docker_id = input('Enter the container ID:  ')
            subprocess.call(command_docker_remove_container + docker_id)
            continue

        if choice == "6":
            choice_docker = input('Enter the image name, Ubuntu, Centos  ').lower()
            if choice_docker == "ubuntu":
                subprocess.call(command_docker_pull_image + 'ubuntu')
            if choice_docker == "Centos":
                subprocess.call(command_docker_pull_image + 'centos')
            continue

        if choice == "7":
            subprocess.call(command_docker_list_image)
            choice_image = input('Enter the image ID:  ').lower()
            subprocess.call(command_docker_remove_image + choice_image)
            continue

        if choice == "9":
            break

def paramiko_connection(ip):
    with open(file_name, 'r') as json_file:
        file_data = json.load(json_file)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(file_data[ip]['ip'], 22, file_data[ip]['user'], file_data[ip]['password'])
        stdin, stdout, stderr = ssh.exec_command(command_version)
        lines = stdout.readlines()
        return lines
        jsonFile.close()

def json_read():
    json_file = open(file_name, 'r')
    json_object = json.load(json_file)
    json_file.close()
    return json_object

def json_write(dict):
    json_file = open(file_name, "w")
    json.dump(dict, json_file, indent=4)
    json_file.close()

def input_data():
    host_input = input('Enter Host Name: ')
    ip_input = input('Enter IP Address:  ')
    user_input = input('Enter User Name:  ')
    password_input = input('Enter User Password:  ')
    return host_input, ip_input, user_input, password_input



main_menu()