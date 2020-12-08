import paramiko, getpass, re, time, boto3

ip_address = "18.194.1.127"
port = 22

commandLs = "ls"
commandVersion = "lsb_release -a"
commandIP = "hostname -I"
command = "apt-get update && apt-get upgrade"
commandWsl = 'wsl'
commandCd = 'cd /tmp/'
commandSSH = "ssh -i TzahiCohenKey.pem ec2-user@ec2-3-125-156-142.eu-central-1.compute.amazonaws.com"
instance_id = 'i-044f46ca1d9501a03'


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