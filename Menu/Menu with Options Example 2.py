### Menu Information ###

from time import sleep

def menu():
    while (True):
        choice1 = input("What is Your choice?  Y/N  \n").lower()
        if(choice1 == ("y")):
            print("You Selected, YES\n\n")
            sleep(1)
            continue
        elif (choice1 == ("yes")):
            print("You Selected, YES\n\n")
            sleep(1)
            continue
        if(choice1 == ("n")):
            choice2 = input("Are You Sure You Want To Exit?  Y/N  \n").lower()
            if(choice2 == ("n")):
                continue
            if(choice2 == ("no")):
                continue
            if(choice2 == ("y")):
                print("\nThank you! Bye Bye.......\n")
                sleep(2)
                break
            if(choice2 == ("yes")):
                print("\nThank you! Bye Bye.......\n")
                sleep(2)
                break
        else:
            print("Unknown Answer..\n\n\n\n")

menu()