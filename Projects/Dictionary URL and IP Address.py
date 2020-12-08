'''
build a dictionary with URL and IP Address
the user can add URL or IP Address to the dictionary in a for loop
the for loop will check if the URL and IP Address is in the dictionary DB
print the dictionary DB to the user

add a way for the user to delete an item from the dictionary
'''
######### Import Information #################

from time import sleep
from itertools import cycle
import threading
import os

######### Dictionary Information ##############

dictList = {"google.com":"1.1.1.1", "msn.com":"2.2.2.2"}

######### Menu Information ####################

def menu():
    while(True):
        choice = input("\n*** Menu ***\n\n1.Add a URL \n2.List DB \n3.Remove URL \n4.Search For IP Address \n--  Press Q to Exit --\n\nSelect:  ").lower()
        if choice == "1":                       ###### Menu Input from User
            for item in range(1):
                item1 = input("Enter a URL:   ").lower()
                item2 = input("Enter an IP:   ").lower()
                print("\nlets search if we have it in our DB")
                SpinnerUI()
                if item1 in dictList:
                    print("\nYes, " + item1 + " is one of the items in the this Dictionary\n")
                    print(dictList)
            else:
                print(item1 + " not in the list, we are adding it\n")
                dictList.update({item1: item2})
                sleep(2)
                print("URL added to our DB Successfully\n")
                print("New List - ", dictList)
                clear()

        if choice == "2":                       ###### Menu Input from User
            SpinnerUI()
            print("\n\n\nListing URL`s in our DB...\n\n",*dictList, sep = ", ")
            print("\n\n")
            clear()

        if choice == "3":                       ###### Menu Input from User
            enterURL = input("Enter a URL to Remove:   ")
            if enterURL in dictList:
                SpinnerUI()
                dictList.pop(enterURL)
                print("IP Removed Successfully..")
                clear()

            else:
                SpinnerUI()
                print("URL in NOT Valid, Please enter a Valid URL address")
                clear()

        if choice == "4":                       ###### Menu Input from User
            searchingDB()

        if choice == "q":                       ###### Menu Input from User
            break

        else:
            # print("Only select: 1, 2, 3, 4 OR Q to Exit")
            os.system('cls')


###############  Definitions   #####################

def SpinnerUI():
    class Spinner:
        __default_spinner_symbols_list = ['|-----|', '|#----|', '|-#---|', '|--#--|', '|---#-|', '|----#|']

        def __init__(self, spinner_symbols_list: [str] = None):
            spinner_symbols_list = spinner_symbols_list if spinner_symbols_list else Spinner.__default_spinner_symbols_list
            self.__screen_lock = threading.Event()
            self.__spinner = cycle(spinner_symbols_list)
            self.__stop_event = False
            self.__thread = None

        def get_spin(self):
            return self.__spinner

        def start(self, spinner_message: str):
            self.__stop_event = False
            time.sleep(0.3)

            def run_spinner(message):
                while not self.__stop_event:
                    print("\r{message} {spinner}".format(message=message, spinner=next(self.__spinner)), end="")
                    time.sleep(0.3)

                self.__screen_lock.set()

            self.__thread = threading.Thread(target=run_spinner, args=(spinner_message,), daemon=True)
            self.__thread.start()

        def stop(self):
            self.__stop_event = True
            if self.__screen_lock.is_set():
                self.__screen_lock.wait()
                self.__screen_lock.clear()
                print("\r", end="")

            print("\r", end="")

    if __name__ == '__main__':
        import time

        # Testing
        spinner = Spinner()
        spinner.start("Working")
        # Make actions
        time.sleep(5)  # Simulate a process
        #
        spinner.stop()

def clear():
    sleep(2)
    os.system("PAUSE")
    os.system('cls')

def searchingDB():
    searchingDB = input("Enter a URL to Search:   ")
    print("\nSearching for it in our DB")
    if searchingDB in dictList:
        print(searchingDB, "in our DataBase, with the IP Address", dictList(1, 2))
        clear()
    else:
        SpinnerUI()
    print(searchingDB, "in not in our DataBase.")
    addToDB = input("Press Y to Add it to the Database\n").lower()
    if (addToDB == "y"):
        item4 = input("Enter the IP of the URL:   ")
        SpinnerUI()
        dictList.update({searchingDB: item4})
        print("IP Added to our DataBase Successfully")
        clear()

menu()