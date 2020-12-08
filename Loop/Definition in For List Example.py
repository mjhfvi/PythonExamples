def IP_LIST():
    list_ip=[]
    for i in range(4):
        list_ip.append(input("Enter an IP: "))
    return list_ip


my_list=IP_LIST()
print("My new list is: " + str(my_list))