
from time import *
from fpdf import *
import random
import json
import os
from Definition_Room import *
######################  General Information   ######################################
Hotel_Text = "** And we will need to move Some of your Group to a Different Hotel **"
S1 = 1
######################  File Path  ####################################################
FolderRootPath = "D:\\HotelProject\\"
FileOrdersPath = "Orders.json"
FileDefinitionPath = "Definition.json"
############  Testing for an Existing Folder ##########################################
try:
    os.mkdir(FolderRootPath)
except OSError:
    print("Directory %s Exists" % FolderRootPath)
else:
    print("Successfully created the directory %s " % FolderRootPath)
############  Testing for an Existing Orders.json File  ###############################
try:
    open(FolderRootPath + FileOrdersPath,)
except IOError:
    FileOrders = open(FolderRootPath + FileOrdersPath, "w+")
    json.dump(UserInputList, FileOrders); FileOrders.write("\n")
    FileOrders.close()
    print("Successfully created the file %s " % FileOrdersPath)
else:
    print("File %s Exists" % FileOrdersPath)
############  Testing for an Existing Definition.json File  and Adding Information if Not  #####
try:
    open(FolderRootPath + FileDefinitionPath,)
except IOError:
    FileDefinition = open(FolderRootPath + FileDefinitionPath, "w+")
    json.dump(Room1_Setai_Hotel, FileDefinition); FileDefinition.write("\n")
    json.dump(Room2_Setai_Hotel, FileDefinition); FileDefinition.write("\n")
    json.dump(Room3_Setai_Hotel, FileDefinition); FileDefinition.write("\n")
    json.dump(Room4_Setai_Hotel, FileDefinition); FileDefinition.write("\n")
    json.dump(Room1_Iris_Hotel, FileDefinition); FileDefinition.write("\n")
    json.dump(Room2_Iris_Hotel, FileDefinition); FileDefinition.write("\n")
    json.dump(Room3_Iris_Hotel, FileDefinition); FileDefinition.write("\n")
    json.dump(Room4_Iris_Hotel, FileDefinition); FileDefinition.write("\n")
    FileDefinition.close()
    print("Successfully created the file %s " % FileDefinitionPath)
else:
    print("File %s Exists" % FileDefinitionPath)
#############  Menu Start  ###########################################################
print("\n***  Welcome To Hotel Ordering  ***")
def Menu():
    while (True):
        list_Item = []
        list_Days_Stay = []
        list_Hotel_Choice = []
        list_Room_Choice = []
        list_Room_Price = []

        choice = input("\n\nSelect from the List:\n\n"
                       "1. Input User Information\n"
                       "2. List Hotels and Rooms Availability  \n"
                       "3. Start Order process  \n"
                       "4. List Orders and Cancel Order   \n"
                       "--Removed--5. Find Available Days for Rooms--   \n\n"
                       "6. -Exit-\n\n")

        if choice =="1":
            UserInputInfo = {'OrderNumber': 0, 'OrderActive': 0, 'FirstName': 0, 'LastName': 0,'AdultsNumber': 0, 'ChildrenNumber': 0, }
            DayToStay = {'Sunday': 0, 'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0}
            First_Name = input("Enter Your First Name:  ").capitalize()
            UserInputInfo.update({'FirstName': First_Name})
            Last_Name = input("Enter Your Last Name:  ").capitalize()
            UserInputInfo.update({'LastName': Last_Name})
            Adults_Number = input("Select Number of Adults:  ");
            UserInputInfo.update({'AdultsNumber': Adults_Number})
            Children_Number = input("Select number of Children:  "); UserInputInfo.update({'ChildrenNumber': Children_Number})

            print("Please Select the Days You want to Stay,")
            inputStaySunday = input("Sunday: Y/N  ").lower()
            DayToStay.update({'Sunday': inputStaySunday})
            inputStayMonday = input("Monday: Y/N  ").lower()
            DayToStay.update({'Monday': inputStayMonday})
            inputStayTuesday = input("Tuesday: Y/N  ").lower()
            DayToStay.update({'Tuesday': inputStayTuesday})
            inputStayWednesday = input("Wednesday: Y/N  ").lower()
            DayToStay.update({'Wednesday': inputStayWednesday})
            inputStayThursday = input("Thursday: Y/N  ").lower()
            DayToStay.update({'Thursday': inputStayThursday})
            UserInputInfo.update(DayToStay)

            Order_Approval = input("\n\n**************************************" +
                                   "\n    Please Approve your Request,       " +
                                   "\n    Full Name is: " + First_Name + " " + Last_Name +
                                   "\n    Number of Adults: " + Adults_Number +
                                   "\n    Number of Children: " + Children_Number +
                                   # "\n    Days of Stay: " + str(len(list_Days_Stay)) +
                                   "\n*************************************\n\n"
                                   "Do You Approve Your Information, Select Y/N\n").lower()
            if Order_Approval == "n":
                print("*** You Canceled Your Information Input ***\n\n")
                sleep(S1)
                continue
            if Order_Approval == "y":
                print("*** Your Information Input Approved ***\n\n")
                UserInputInfo.update({'OrderActive': 1})
                FileOrders = open(FolderRootPath + FileOrdersPath, "a")
                json.dump(UserInputInfo, FileOrders); FileOrders.write("\n"); FileOrders.close()
                sleep(S1)

                Choice_Hotel = input("Select the Hotel: \n"
                                     "1. Hotel Setai \n"
                                     "2. Hotel Iris \n")

                if Choice_Hotel == "1":  ## Hotel Selection and Price
                    print("Your Hotel Selection is --Setai--\n***** Recommended Rooms For You ***************  ")

                if Choice_Hotel == "2":  ## Hotel Selection and Price
                    print("Your Hotel Selection is --Iris--\n***** Recommended Rooms For You ***************  ")



Menu()