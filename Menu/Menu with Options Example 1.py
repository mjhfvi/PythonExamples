### Menu Information ###

from time import sleep

while(True):
    choice = input("\nMenu:\n1.Option 1:\n2.Option 2: \n3.Option 3:\n4.Option 4:\n5.Option 5:\n")
    if choice == "1":
        for item in range(11):
            print(item)
    elif choice == "2":
        for item in range(21):
            print(item)
    elif choice == "3":
        for item in range(31):
            print(item)
    elif choice == "4":
        for item in range(41):
            print(item)
    elif choice == "5":
        for item in range(51):
            print(item)
    else:
        print("Only select: 1 or 2 or 3 or 4 or 5")
        sleep(2)
        continue
    if input("Do You Want To Exit?  Y/N \n\n").lower()=="y":
        break
    else:
        print("Unknown Answer..\n")
        sleep(2)
        print("Starting Again....")
        sleep(2)
        continue
print("\nBye Bye...")
sleep(2)