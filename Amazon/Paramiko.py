import base64
import paramiko

key = paramiko.RSAKey(data=base64.b64decode(b'AAA...'))
client = paramiko.SSHClient()
client.get_host_keys().add('ssh.example.com', 'ssh-rsa', key)
client.connect('ssh.example.com', username='strongbad', password='thecheat')
stdin, stdout, stderr = client.exec_command('ls')
for line in stdout:
    print('... ' + line.strip('\n'))
client.close()


def ssh_connect_with_retry(ssh, ip_address, retries):
    if retries > 3:
        return False
    privkey = paramiko.RSAKey.from_private_key_file('/tmp/TzahiCohenKey.pem')
    interval = 5
    try:
        retries += 1
        print('SSH into the instance: {}'.format(ip_address))
        ssh.connect(hostname=ip_address, username='ec2-user', pkey=privkey)
        return True
    except Exception as e:
        print(e)
        sleep(4)
        print('Retrying SSH connection to {}'.format(ip_address))
        ssh_connect_with_retry(ssh, ip_address, retries)

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
