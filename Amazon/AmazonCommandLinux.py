'''
Commands Page
'''

############  Ubuntu Commands  #############################################################
command_ubuntu_update = "apt-get update"
command_ubuntu_upgrade = "apt-get upgrade"
command_ubuntu_install_apt_get = "apt-get install"

############  CentOS/Fedora Commands  ######################################################
command_centos_update = "yum check-update && yum update"
command_centos_install_yum = "yum install"

############  System Commands  #############################################################
command_ls = "ls"
command_version = "hostnamectl"
command_ip_addr = "ip addr"
command_computer_host = "hostnamectl"
command_network_scan = "nmap 192.168.50.1-100"

############  Software Install Commands  ####################################################
command_install_python = "python3 python3-pip"
command_install_python_tools = "python3-boto3 python3-paramiko"
command_install_awscli = "awscli"
command_install_nmap = "nmap"
command_install_netperf = "netperf"
command_install_network_tools = "nmap netperf net-tools"
command_install_docker = "docker.io"
command_install_virtualbox = "virtualbox virtualbox-ext-pack"
command_install_nagios = "monitoring-plugins nagios-nrpe-plugin"

############  Zabbix Agent Install Commands  ##########################
command_install_repo_zabbix = "wget https://repo.zabbix.com/zabbix/4.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_4.0-2+bionic_all.deb"
command_install_zabbix = "sudo dpkg -i zabbix-release_4.0-2+bionic_all.deb"


############  Docker Commands  #############################################################
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

############  VirtualBox Commands  #############################################################
command_virtualbox_list = ["VBoxManage", 'list', 'vms']
command_virtualbox_list_running = ["vboxmanage", 'list', 'runningvms']
command_virtualbox_list_ostypes = ["VBoxManage", 'list', 'ostypes']

############  Repository Commands  #############################################################
repo_ubuntu_key_chrome = "wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add - "
# repo_ubuntu_aptfile_chrome =  "sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'"





