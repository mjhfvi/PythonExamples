'''
IP Address System
1. get IP address from user
2. test IP address
'''

ipaddressList = []
for x in range(1):
    Inputipadress = input("Enter Your IP address: ")
    while ("127.0.0.0" in Inputipadress or >255 in Inputipadress):
        print("invalid number please input anther number: ")
        Inputipadress = input("Enter Your IP address: ")
    ipaddressList.append(Inputipadress)
    print("your ip address is: " + str(ipaddressList))

#
# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")