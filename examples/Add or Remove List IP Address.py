'''
Get 6 IP address loop to a list
    then search the IP address in the list,
        add new IP address in the list,
            if you dont have it
        remove IP address from the list
    print all the IP address
'''

from time import sleep

listIP = ["1.2", "2.3"]

while(True):
    print("\n** Welcome **\nPlease Enter 6 IP Address to our Database")
    for item in range(6):
        newInput = input("Enter IP address:  ")
        if newInput in listIP:
            sleep(1)
            print("IP in our DataBase, ")
            choice = input("do you want to remove it? press Y to remove the IP address\n").lower()
            if choice == "y":
                listIP.remove(newInput)
        else:
            sleep(2)
            print("IP not in DB, Adding it")
            listIP.append(newInput)

    print("New Database Information:", str(listIP))
    sleep(2)
