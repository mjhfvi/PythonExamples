#!/bin/bash

echo -e "Menu:\n1.Pull Image\n2.Run X Ubuntu\n3.Remove Image/Container\n4.Run Web app Specify Port number\n"
read choice
if [ $choice == "1"]
then
    echo -e "Choose Image to Install: php/ubuntu/centos\n"
    read OS
    while true
    do
    if [$OS == "centos" ] || [$OS == "php" ] || [ $OS == "ubuntu" ]
    then
        sudo docker pull $OS
        break
    else
        echo -e "Enter good OS\n"
    fi
    done
elif [ $choice == "2" ]
then
    echo -e "Enter how many Ubuntus containers you want?"
    read num
    for i in {1..$num}
    do
        sudo docker run -d ubuntu /bin/bash -c 'while true ; do echo net4u ; sleep 1 ; done'
    done
    sudo docker ps

elif  [ %choice == "3" ]
then
    echo -e "Choose image to delete: php/ubuntu/centos\n"
    read OS
    while true
    do
    if [ $OS == "centos" ] || [ $OS == "php"] || [ $OS == "ubuntu" ]
    then
        
    done