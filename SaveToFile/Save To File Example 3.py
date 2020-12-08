'''
start a file net4u.txt on D drive
close the file

open the file with r+ permissions and add 2 ip address from user input
close the file

open the file with read permissions and print it to the screen
close the file

open the file with append permissions and add 2 more ip address from user
close the file

print it again
'''

fileName = "D:\\net4u.txt"

file = open(fileName, "w+")      # x will create new file and NOT overwrite the file is you have it
file.close()

file = open(fileName, "r+")
for i in range(2):
    file.write(input("Enter your IP Address:  ") + "\n")
file.close()

file = open(fileName, "r")
print(file.read())

file = open(fileName, "a")
for i in range(2):
    file.write(input("Enter your IP Address:  ") + "\n")
file.close()

file = open(fileName, "r")
print("\n\nList of IP Address:  \n"+file.read())