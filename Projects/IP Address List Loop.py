'''

For loop to add 5 IP address,
check if you have the IP address in the list
if you have it in the list print "this ip isn't available" and append to the list
if you dont have it in the list print "this ip added to the list"
at the end print the list

'''

ipadds = []
for i in range(5):
    ipadds.append(input("input your ip address: "))

newipadds = input("\ninput a new ip address: ")
print("this ip is already occupied")
# else:
#     print("this ip is aviliable" + "\naddin to the list..")
#     ipadds.append(newipadds)

print("your new list\n")
print(ipadds)
print("\nIt includes " + str(len(ipadds)) + " IPs")

