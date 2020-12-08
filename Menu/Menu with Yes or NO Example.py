### Menu Information ###

from time import sleep

while (True):
    print("Wanna Play a Game?.... ")
    item = input("Yes or No: \n").lower()
    if item == "yes":
        print("OK, Starting the Game\n")
        sleep(1)
        continue
    elif item == "y":
        print("OK, Starting the Game\n")
        sleep(1)
        continue
    elif item == "no":
        print("Bye Bye....")
        sleep(2)
        break
    elif item == "n":
        print("Bye Bye....")
        sleep(2)
        break
    else:
        print("Unknown Answer..\n\n\n\n")