### Functions Example ###

def function1(firstName,lastName):
    print("my name is: " + firstName + ", " + lastName)


choice = input("Printing your name? y/n  \n")
if(choice=="y"):
    function1(input("enter your first name:\n"),input("your last name: \n"))
