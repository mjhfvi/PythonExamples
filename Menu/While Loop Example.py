### Loop Information ###

from time import sleep

list = []
item = ()
while item != 4:
    item = int(input("Search A Number in the List: "))
    list.append(item)
print("You Hit Number 4, Exiting the Application....")
sleep(3)