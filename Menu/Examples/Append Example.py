'''
build a user input menu
1. input from user name and age
2. input list of names(4), check if they are on the list
'''

listNames = []

nameItem = input("Enter your name:  ")
listNames.append(nameItem)
lastNameItem = input("Enter your last Name:  ")
listNames.append(lastNameItem)
ageItem = input("Enter your Age:  ")
listNames.append(ageItem)

choice3 = input("Printing your name? Y/N  \n").lower()
if(choice3 == "y"):
    print(listNames)
else:
    print("Bye Bye....")