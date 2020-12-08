from time import *
from fpdf import *
import random
import os

Hotel_Text = "** And we will need to move Some of your Group to a Different Hotel **"
S1 = 2

print("\n***  Welcome To Hotel Ordering  ***")
def Menu():
    while (True):
        Room1_Setai_Hotel = {'Sunday': 0, 'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0}
        Room2_Setai_Hotel = {'Sunday': 0, 'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0}
        Room3_Setai_Hotel = {'Sunday': 0, 'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0}
        Room4_Setai_Hotel = {'Sunday': 0, 'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0}

        Room1_Iris_Hotel = {'Sunday': 0, 'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0}
        Room2_Iris_Hotel = {'Sunday': 0, 'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0}
        Room3_Iris_Hotel = {'Sunday': 0, 'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0}
        Room4_Iris_Hotel = {'Sunday': 0, 'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0}

        choice = input("\n\nSelect from the List:\n\n"
                       "1. List Hotels and Rooms  \n"
                       "2. Start Order process  \n"
                       "3. List Orders and Cancel Order   \n"
                       "4. Find Available Room  \n\n"
                       "5. -Exit-\n\n")

        if choice == "1":           ## List Hotels and Rooms
            print('Printing all the Hotels and Available Rooms.... ')
            sleep(S1)
            print(Room1234_Satai_Definition)
            print(Room1234_Iris_Definition)
            sleep(S1)
            os.system('cls')
            continue

        if choice == "2":           ## Start Order process
            print("Starting Your Order Process...\n")
            sleep(S1)
            os.system('cls')
            while (True):
                list = []
                list_Room_Price = []

                First_Name = input("Enter Your First Name:  ").capitalize()
                Last_Name = input("Enter Your Last Name:  ").capitalize()
                Adults_Number = input("Select Number of Adults:  ")
                list.append(Adults_Number)
                Children_Number = input("Select number of Children:  ")
                list.append(Children_Number)
                Choice_Days = int(input("Select Number Days To Stay in a Week, (Sun-Thu):  "))
                Order_Approval = input("\n\n**************************************" +
                                       "\n    Please Approve your Request,       " +
                                       "\n    Full Name is: " + First_Name + " " + Last_Name +
                                       "\n    Number of Adults: " + Adults_Number +
                                       "\n    Number of Children: " + Children_Number +
                                       "\n    Days of Stay: " + str(Choice_Days) +
                                       "\n*************************************\n\n"
                                       "Do You Approve Your Information, Select Y/N\n").lower()
                if Order_Approval == "n":
                    print("*** You Canceled Your Information Input ***\n\n")
                    sleep(S1)
                    continue
                if Order_Approval == "y":
                    print("Your Information Input Approved\n\n")
                    sleep(S1)
                    Choice_Hotel = input("Select the Hotel: \n"
                                         "1. Hotel Setai \n"
                                         "2. Hotel Iris \n")

                    if Choice_Hotel == "1":
                        print("Your Hotel Selection is --Setai--\n***** Recommended Rooms For You ***************  ")
                        if list == ['1', '']:
                            print(Room1_Satai_Definition); list_Room_Price = Room1_Satai_Price
                            break
                        if list == ['1', '0']:
                            print(Room1_Satai_Definition); list_Room_Price = Room1_Satai_Price
                            break
                        if list == ['1', '1']:
                            print(Room1_Satai_Definition); list_Room_Price = Room1_Satai_Price
                            break
                        if list == ['1', '2']:
                            print(Room4_Satai_Definition); list_Room_Price = Room4_Satai_Price
                            break
                        if list == ['2', '']:
                            print(Room1_Satai_Definition); list_Room_Price = Room1_Satai_Price
                            break
                        if list == ['2', '0']:
                            print(Room1_Satai_Definition); list_Room_Price = Room1_Satai_Price
                            break
                        if list == ['2', '1']:
                            print(Room2_Satai_Definition); list_Room_Price = Room2_Satai_Price
                            break
                        if list == ['2', '2']:
                            print(Room4_Satai_Definition); list_Room_Price = Room4_Satai_Price
                            break
                        if list == ['2', '3']:
                            print(Room14_Satai_Definition); list_Room_Price = Room14_Satai_Price
                            break
                        if list == ['2', '4']:
                            print(Room4_Satai_Definition + Hotel_Text + Room4_Iris_Definition); list_Room_Price = Room4_Satai_Price + Room4_Iris_Price
                            break
                        if list == ['3', '']:
                            print(Room3_Satai_Definition); list_Room_Price = Room3_Satai_Price
                            break
                        if list == ['3', '0']:
                            print(Room3_Satai_Definition); list_Room_Price = Room3_Satai_Price
                            break
                        if list == ['3', '1']:
                            print(Room12_Satai_Definition); list_Room_Price = Room12_Satai_Price
                            break
                        if list == ['3', '2']:
                            print(Room12_Satai_Definition); list_Room_Price = Room12_Satai_Price
                            break
                        if list == ['3', '3']:
                            print(Room24_Satai_Definition); list_Room_Price = Room24_Satai_Price
                            break
                        if list == ['3', '4']:
                            print(Room124_Satai_Definition); list_Room_Price = Room124_Satai_Price
                            break
                        if list == ['3', '5']:
                            print(Room14_Satai_Definition); list_Room_Price = Room14_Satai_Price
                            break
                        if list == ['4', '']:
                            print(Room24_Satai_Definition); list_Room_Price = Room24_Satai_Price
                            break
                        if list == ['4', '0']:
                            print(Room24_Satai_Definition); list_Room_Price = Room24_Satai_Price
                            break
                        if list == ['4', '1']:
                            print(Room24_Satai_Definition); list_Room_Price = Room24_Satai_Price
                            break
                        if list == ['4', '2']:
                            print(Room24_Satai_Definition); list_Room_Price = Room24_Satai_Price
                            break
                        if list == ['4', '3']:
                            print(Room24_Satai_Definition); list_Room_Price = Room24_Satai_Price
                            break
                        if list == ['4', '4']:
                            print(Room4_Satai_Definition + Hotel_Text + Room4_Iris_Definition); list_Room_Price = Room4_Satai_Price + Room4_Iris_Price
                            break
                        if list == ['4', '5']:
                            print(Room124_Satai_Definition + Hotel_Text + Room1_Iris_Definition); list_Room_Price = Room124_Satai_Price + Room1_Iris_Price
                            break
                        if list == ['4', '6']:
                            print(Room124_Satai_Definition + Hotel_Text + Room4_Iris_Definition); list_Room_Price = Room124_Satai_Price + Room4_Iris_Price
                            break
                        if list == ['4', '7']:
                            print(Room124_Satai_Definition + Hotel_Text + Room4_Iris_Definition); list_Room_Price = Room124_Satai_Price + Room4_Iris_Price
                            break
                        if list == ['4', '8']:
                            print(Room124_Satai_Definition + Hotel_Text + Room124_Iris_Definition); list_Room_Price = Room124_Satai_Price + Room124_Iris_Price
                            break
                        if list == ['5', '']:
                            print(Room23_Satai_Definition); list_Room_Price = Room23_Satai_Price
                            break
                        if list == ['5', '0']:
                            print(Room23_Satai_Definition); list_Room_Price = Room23_Satai_Price
                            break
                        if list == ['5', '1']:
                            print(Room23_Satai_Definition); list_Room_Price = Room23_Satai_Price
                            break
                        if list == ['5', '2']:
                            print(Room34_Satai_Definition); list_Room_Price = Room34_Satai_Price
                            break
                        if list == ['5', '3']:
                            print(Room134_Satai_Definition); list_Room_Price = Room134_Satai_Price
                            break
                        if list == ['5', '4']:
                            print(Room124_Satai_Definition); list_Room_Price = Room124_Satai_Price
                            break
                        if list == ['5', '5']:
                            print(Room1234_Satai_Definition); list_Room_Price = Room1234_Satai_Price
                            break
                        if list == ['5', '6']:
                            print(Room124_Satai_Definition + Hotel_Text + Room4_Iris_Definition); list_Room_Price = Room124_Satai_Price
                            break
                        if list == ['5', '7']:
                            print(Room124_Satai_Definition + Hotel_Text + Room124_Iris_Definition); list_Room_Price = Room124_Satai_Price
                            break
                        if list == ['5', '8']:
                            print(Room124_Satai_Definition + Hotel_Text + Room124_Iris_Definition); list_Room_Price = Room124_Satai_Price
                            break
                        if list == ['6', '']:
                            print(Room123_Satai_Definition); list_Room_Price = Room123_Satai_Price
                            break
                        if list == ['6', '0']:
                            print(Room123_Satai_Definition); list_Room_Price = Room123_Satai_Price
                            break
                        if list == ['6', '1']:
                            print(Room123_Satai_Definition); list_Room_Price = Room123_Satai_Price
                            break
                        if list == ['6', '2']:
                            print(Room123_Satai_Definition); list_Room_Price = Room123_Satai_Price
                            break
                        if list == ['6', '3']:
                            print(Room234_Satai_Definition); list_Room_Price = Room234_Satai_Price
                            break
                        if list == ['6', '4']:
                            print(Room234_Satai_Definition); list_Room_Price = Room234_Satai_Price
                            break
                        if list == ['6', '5']:
                            print(Room234_Satai_Definition + Hotel_Text + Room4_Iris_Definition); list_Room_Price = Room234_Satai_Price + Room4_Iris_Price
                            break
                        if list == ['6', '6']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room4_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room4_Iris_Price
                            break
                        if list == ['6', '7']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room14_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room14_Iris_Price
                            break
                        if list == ['6', '8']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room124_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room124_Iris_Price
                            break
                        if list == ['7', '']:
                            print(Room234_Satai_Definition); list_Room_Price = Room234_Satai_Price
                            break
                        if list == ['7', '0']:
                            print(Room234_Satai_Definition); list_Room_Price = Room234_Satai_Price
                            break
                        if list == ['7', '1']:
                            print(Room234_Satai_Definition); list_Room_Price = Room234_Satai_Price
                            break
                        if list == ['7', '2']:
                            print(Room234_Satai_Definition); list_Room_Price = Room234_Satai_Price
                            break
                        if list == ['7', '3']:
                            print(Room234_Satai_Definition); list_Room_Price = Room234_Satai_Price
                            break
                        if list == ['7', '4']:
                            print(Room1234_Satai_Definition); list_Room_Price = Room1234_Satai_Price
                            break
                        if list == ['7', '5']:
                            print(Room234_Satai_Definition + Hotel_Text + Room1_Iris_Definition); list_Room_Price = Room234_Satai_Price + Room1_Iris_Price
                            break
                        if list == ['7', '6']:
                            print(Room234_Satai_Definition + Hotel_Text + Room4_Iris_Definition); list_Room_Price = Room234_Satai_Price + Room4_Iris_Price
                            break
                        if list == ['7', '7']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room4_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room4_Iris_Price
                            break
                        if list == ['7', '8']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room124_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room124_Iris_Price
                            break
                        if list == ['8', '']:
                            print(Room1234_Satai_Definition); list_Room_Price = Room1234_Satai_Price
                            break
                        if list == ['8', '0']:
                            print(Room1234_Satai_Definition); list_Room_Price = Room1234_Satai_Price
                            break
                        if list == ['8', '1']:
                            print(Room1234_Satai_Definition); list_Room_Price = Room1234_Satai_Price
                            break
                        if list == ['8', '2']:
                            print(Room1234_Satai_Definition); list_Room_Price = Room1234_Satai_Price
                            break
                        if list == ['8', '3']:
                            print(Room1234_Satai_Definition); list_Room_Price = Room1234_Satai_Price
                            break
                        if list == ['8', '4']:
                            print(Room1234_Satai_Definition); list_Room_Price = Room1234_Satai_Price
                            break
                        if list == ['8', '5']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room1_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room1_Iris_Price
                            break
                        if list == ['8', '6']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room4_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room4_Iris_Price
                            break
                        if list == ['8', '7']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room14_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room14_Iris_Price
                            break
                        if list == ['8', '8']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room124_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room124_Iris_Price
                            break
                        if list == ['9', '']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room1_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room1_Iris_Price
                            break
                        if list == ['9', '0']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room1_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room1_Iris_Price
                            break
                        if list == ['9', '1']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room1_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room1_Iris_Price
                            break
                        if list == ['9', '2']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room1_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room1_Iris_Price
                            break
                        if list == ['9', '3']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room1_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room1_Iris_Price
                            break
                        if list == ['9', '4']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room1_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room1_Iris_Price
                            break
                        if list == ['9', '5']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room1_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room1_Iris_Price
                            break
                        if list == ['9', '6']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room4_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room4_Iris_Price
                            break
                        if list == ['9', '7']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room14_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room14_Iris_Price
                            break
                        if list == ['9', '8']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room124_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room124_Iris_Price
                            break
                        if list == ['10', '']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room2_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room2_Iris_Price
                            break
                        if list == ['10', '0']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room2_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room2_Iris_Price
                            break
                        if list == ['10', '1']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room2_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room2_Iris_Price
                            break
                        if list == ['10', '2']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room2_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room2_Iris_Price
                            break
                        if list == ['10', '3']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room2_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room2_Iris_Price
                            break
                        if list == ['10', '4']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room2_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room2_Iris_Price
                            break
                        if list == ['10', '5']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room2_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room2_Iris_Price
                            break
                        if list == ['10', '6']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room12_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room12_Iris_Price
                            break
                        if list == ['10', '7']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room14_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room14_Iris_Price
                            break
                        if list == ['10', '8']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room124_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room124_Iris_Price
                            break
                        if list == ['11', '']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room3_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room3_Iris_Price
                            break
                        if list == ['11', '0']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room3_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room3_Iris_Price
                            break
                        if list == ['11', '1']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room3_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room3_Iris_Price
                            break
                        if list == ['11', '2']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room3_Iris_Definition); list_Room_Price = Room1_Satai_Price + Room3_Iris_Price
                            break
                        if list == ['11', '3']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room3_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room3_Iris_Price
                            break
                        if list == ['11', '4']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room3_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room3_Iris_Price
                            break
                        if list == ['11', '5']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room13_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room13_Iris_Price
                            break
                        if list == ['11', '6']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room34_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room34_Iris_Price
                            break
                        if list == ['11', '7']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room134_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room134_Iris_Price
                            break
                        if list == ['11', '8']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room134_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room134_Iris_Price
                            break
                        if list == ['12', '']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room12_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room12_Iris_Price
                            break
                        if list == ['12', '0']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room12_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room12_Iris_Price
                            break
                        if list == ['12', '1']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room12_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room12_Iris_Price
                            break
                        if list == ['12', '2']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room12_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room12_Iris_Price
                            break
                        if list == ['12', '3']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room12_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room12_Iris_Price
                            break
                        if list == ['12', '4']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room12_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room12_Iris_Price
                            break
                        if list == ['12', '5']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room12_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room12_Iris_Price
                            break
                        if list == ['12', '6']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room14_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room14_Iris_Price
                            break
                        if list == ['12', '7']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room1234_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room1234_Iris_Price
                            break
                        if list == ['12', '8']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room234_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room234_Iris_Price
                            break
                        if list == ['13', '']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room234_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room234_Iris_Price
                            break
                        if list == ['13', '0']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room234_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room234_Iris_Price
                            break
                        if list == ['13', '1']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room234_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room234_Iris_Price
                            break
                        if list == ['13', '2']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room234_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room234_Iris_Price
                            break
                        if list == ['13', '3']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room234_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room234_Iris_Price
                            break
                        if list == ['13', '4']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room234_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room234_Iris_Price
                            break
                        if list == ['13', '5']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room234_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room234_Iris_Price
                            break
                        if list == ['13', '6']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room1234_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room1234_Iris_Price
                            break
                        if list == ['13', '7']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room1234_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room1234_Iris_Price
                            break
                        if list == ['13', '8']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room1234_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room1234_Iris_Price
                            break
                        if list == ['14', '']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room1234_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room1234_Iris_Price
                            break
                        if list == ['14', '0']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room1234_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room1234_Iris_Price
                            break
                        if list == ['14', '1']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room1234_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room1234_Iris_Price
                            break
                        if list == ['14', '2']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room1234_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room1234_Iris_Price
                            break
                        if list == ['14', '3']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room1234_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room1234_Iris_Price
                            break
                        if list == ['14', '4']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room1234_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room1234_Iris_Price
                            break
                        if list == ['14', '5']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room1234_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room1234_Iris_Price
                            break
                        if list == ['14', '6']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room1234_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room1234_Iris_Price
                            break
                        if list == ['14', '7']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room1234_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room1234_Iris_Price
                            break
                        if list == ['14', '8']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room1234_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room1234_Iris_Price
                            break
                        if list == ['14', '1']:
                            print(Room1234_Satai_Definition + Hotel_Text + Room1234_Iris_Definition); list_Room_Price = Room1234_Satai_Price + Room1234_Iris_Price
                            break

                        # else:
                        #     print("Your Request Exceed Our Room Capacity Or you Entered Invalid Value")

                    if Choice_Hotel == "2":
                        print("Your Hotel Selection is --Iris--\n***** Recommended Rooms For You ***************  ")
                        if list == ['1', '']:print(Room1_Iris_Definition); list_Room_Price = Room1_Iris_Price
                        break
                        if list == ['1', '0']:print(Room1_Iris_Definition); list_Room_Price = Room1_Iris_Price
                        break
                        if list == ['1', '1']:
                            print(Room1_Iris_Definition); list_Room_Price = Room1_Iris_Price
                            break
                        if list == ['1', '2']:
                            print(Room4_Iris_Definition); list_Room_Price = Room4_Iris_Price
                            break
                        if list == ['2', '']:
                            print(Room1_Iris_Definition); list_Room_Price = Room1_Iris_Price
                            break
                        if list == ['2', '0']:
                            print(Room1_Iris_Definition); list_Room_Price = Room1_Iris_Price
                            break
                        if list == ['2', '1']:
                            print(Room2_Iris_Definition); list_Room_Price = Room2_Iris_Price
                            break
                        if list == ['2', '2']:
                            print(Room4_Iris_Definition); list_Room_Price = Room4_Iris_Price
                            break
                        if list == ['2', '3']:
                            print(Room14_Iris_Definition); list_Room_Price = Room14_Iris_Price
                            break
                        if list == ['2', '4']:
                            print(Room4_Iris_Definition + Hotel_Text + Room4_Satai_Definition); list_Room_Price = Room4_Iris_Price + Room4_Satai_Price
                            break
                        if list == ['3', '']:
                            print(Room3_Iris_Definition); list_Room_Price = Room3_Iris_Price
                            break
                        if list == ['3', '0']:
                            print(Room3_Iris_Definition); list_Room_Price = Room3_Iris_Price
                            break
                        if list == ['3', '1']:
                            print(Room12_Iris_Definition); list_Room_Price = Room12_Iris_Price
                            break
                        if list == ['3', '2']:
                            print(Room12_Iris_Definition); list_Room_Price = Room12_Iris_Price
                            break
                        if list == ['3', '3']:
                            print(Room24_Iris_Definition); list_Room_Price = Room24_Iris_Price
                            break
                        if list == ['3', '4']:
                            print(Room124_Iris_Definition); list_Room_Price = Room124_Iris_Price
                            break
                        if list == ['3', '5']:
                            print(Room14_Iris_Definition); list_Room_Price = Room14_Iris_Price
                            break
                        if list == ['4', '']:
                            print(Room24_Iris_Definition); list_Room_Price = Room24_Iris_Price
                            break
                        if list == ['4', '0']:
                            print(Room24_Iris_Definition); list_Room_Price = Room24_Iris_Price
                            break
                        if list == ['4', '1']:
                            print(Room24_Iris_Definition); list_Room_Price = Room1_Iris_Price
                            break
                        if list == ['4', '2']:
                            print(Room24_Iris_Definition); list_Room_Price = Room24_Iris_Price
                            break
                        if list == ['4', '3']:
                            print(Room24_Iris_Definition); list_Room_Price = Room24_Iris_Price
                            break
                        if list == ['4', '4']:
                            print(Room4_Iris_Definition + Hotel_Text + Room4_Satai_Definition); list_Room_Price = Room4_Iris_Price + Room4_Satai_Price
                            break
                        if list == ['4', '5']:
                            print(Room124_Iris_Definition + Hotel_Text + Room1_Satai_Definition); list_Room_Price = Room134_Iris_Price + Room1_Satai_Price
                            break
                        if list == ['4', '6']:
                            print(Room124_Iris_Definition + Hotel_Text + Room4_Satai_Definition); list_Room_Price = Room124_Iris_Price + Room4_Satai_Price
                            break
                        if list == ['4', '7']:
                            print(Room124_Iris_Definition + Hotel_Text + Room4_Satai_Definition); list_Room_Price = Room124_Iris_Price + Room4_Satai_Price
                            break
                        if list == ['4', '8']:
                            print(Room124_Iris_Definition + Hotel_Text + Room124_Satai_Definition); list_Room_Price = Room124_Iris_Price + Room124_Satai_Price
                            break
                        if list == ['5', '']:
                            print(Room23_Iris_Definition); list_Room_Price = Room23_Iris_Price
                            break
                        if list == ['5', '0']:
                            print(Room23_Iris_Definition); list_Room_Price = Room23_Iris_Price
                            break
                        if list == ['5', '1']:
                            print(Room23_Iris_Definition); list_Room_Price = Room23_Iris_Price
                            break
                        if list == ['5', '2']:
                            print(Room34_Iris_Definition); list_Room_Price = Room34_Iris_Price
                            break
                        if list == ['5', '3']:
                            print(Room134_Iris_Definition); list_Room_Price = Room134_Iris_Price
                            break
                        if list == ['5', '4']:
                            print(Room124_Iris_Definition); list_Room_Price = Room124_Iris_Price
                            break
                        if list == ['5', '5']:
                            print(Room1234_Iris_Definition); list_Room_Price = Room1234_Iris_Price
                            break
                        if list == ['5', '6']:
                            print(Room124_Iris_Definition + Hotel_Text + Room4_Satai_Definition); list_Room_Price = Room124_Iris_Price + Room4_Satai_Price
                            break
                        if list == ['5', '7']:
                            print(Room124_Iris_Definition + Hotel_Text + Room124_Satai_Definition); list_Room_Price = Room124_Iris_Price + Room124_Satai_Price
                            break
                        if list == ['5', '8']:
                            print(Room124_Iris_Definition + Hotel_Text + Room124_Satai_Definition); list_Room_Price = Room124_Iris_Price + Room124_Satai_Price
                            break
                        if list == ['6', '']:
                            print(Room123_Iris_Definition); list_Room_Price = Room123_Iris_Price
                            break
                        if list == ['6', '0']:
                            print(Room123_Iris_Definition); list_Room_Price = Room123_Iris_Price
                            break
                        if list == ['6', '1']:
                            print(Room123_Iris_Definition); list_Room_Price = Room123_Iris_Price
                            break
                        if list == ['6', '2']:
                            print(Room123_Iris_Definition); list_Room_Price = Room123_Iris_Price
                            break
                        if list == ['6', '3']:
                            print(Room234_Iris_Definition); list_Room_Price = Room234_Iris_Price
                            break
                        if list == ['6', '4']:
                            print(Room234_Iris_Definition); list_Room_Price = Room234_Iris_Price
                            break
                        if list == ['6', '5']:
                            print(Room234_Iris_Definition + Hotel_Text + Room4_Satai_Definition); list_Room_Price = Room234_Iris_Price + Room4_Satai_Price
                            break
                        if list == ['6', '6']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room4_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room4_Satai_Price
                            break
                        if list == ['6', '7']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room14_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room14_Satai_Price
                            break
                        if list == ['6', '8']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room124_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room124_Satai_Price
                            break
                        if list == ['7', '']:
                            print(Room234_Iris_Definition); list_Room_Price = Room234_Iris_Price
                            break
                        if list == ['7', '0']:
                            print(Room234_Iris_Definition); list_Room_Price = Room234_Iris_Price
                            break
                        if list == ['7', '1']:
                            print(Room234_Iris_Definition); list_Room_Price = Room234_Iris_Price
                            break
                        if list == ['7', '2']:
                            print(Room234_Iris_Definition); list_Room_Price = Room234_Iris_Price
                            break
                        if list == ['7', '3']:
                            print(Room234_Iris_Definition); list_Room_Price = Room234_Iris_Price
                            break
                        if list == ['7', '4']:
                            print(Room1234_Iris_Definition); list_Room_Price = Room1234_Iris_Price
                            break
                        if list == ['7', '5']:
                            print(Room234_Iris_Definition + Hotel_Text + Room1_Satai_Definition); list_Room_Price = Room234_Iris_Price + Room1_Satai_Price
                            break
                        if list == ['7', '6']:
                            print(Room234_Iris_Definition + Hotel_Text + Room4_Satai_Definition); list_Room_Price = Room234_Iris_Price + Room4_Satai_Price
                            break
                        if list == ['7', '7']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room4_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room4_Satai_Price
                            break
                        if list == ['7', '8']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room124_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room124_Satai_Price
                            break
                        if list == ['8', '']:
                            print(Room1234_Iris_Definition); list_Room_Price = Room1234_Iris_Price
                            break
                        if list == ['8', '0']:
                            print(Room1234_Iris_Definition); list_Room_Price = Room1234_Iris_Price
                            break
                        if list == ['8', '1']:
                            print(Room1234_Iris_Definition); list_Room_Price = Room1234_Iris_Price
                            break
                        if list == ['8', '2']:
                            print(Room1234_Iris_Definition); list_Room_Price = Room1234_Iris_Price
                            break
                        if list == ['8', '3']:
                            print(Room1234_Iris_Definition); list_Room_Price = Room1234_Iris_Price
                            break
                        if list == ['8', '4']:
                            print(Room1234_Iris_Definition); list_Room_Price = Room1234_Iris_Price
                            break
                        if list == ['8', '5']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room1_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room1_Satai_Price
                            break
                        if list == ['8', '6']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room4_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room1_Satai_Price
                            break
                        if list == ['8', '7']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room14_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room1_Satai_Price
                            break
                        if list == ['8', '8']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room124_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room1_Satai_Price
                            break
                        if list == ['9', '']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room1_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room1_Satai_Price
                            break
                        if list == ['9', '0']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room1_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room1_Satai_Price
                            break
                        if list == ['9', '1']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room1_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room1_Satai_Price
                            break
                        if list == ['9', '2']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room1_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room1_Satai_Price
                            break
                        if list == ['9', '3']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room1_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room1_Satai_Price
                            break
                        if list == ['9', '4']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room1_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room1_Satai_Price
                            break
                        if list == ['9', '5']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room1_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room1_Satai_Price
                            break
                        if list == ['9', '6']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room4_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room4_Satai_Price
                            break
                        if list == ['9', '7']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room14_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room14_Satai_Price
                            break
                        if list == ['9', '8']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room124_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room124_Satai_Price
                            break
                        if list == ['10', '']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room2_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room2_Satai_Price
                            break
                        if list == ['10', '0']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room2_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room2_Satai_Price
                            break
                        if list == ['10', '1']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room2_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room2_Satai_Price
                            break
                        if list == ['10', '2']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room2_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room2_Satai_Price
                            break
                        if list == ['10', '3']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room2_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room2_Satai_Price
                            break
                        if list == ['10', '4']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room2_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room2_Satai_Price
                            break
                        if list == ['10', '5']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room2_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room2_Satai_Price
                            break
                        if list == ['10', '6']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room12_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room12_Satai_Price
                            break
                        if list == ['10', '7']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room14_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room14_Satai_Price
                            break
                        if list == ['10', '8']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room124_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room124_Satai_Price
                            break
                        if list == ['11', '']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room3_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room13_Satai_Price
                            break
                        if list == ['11', '0']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room3_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room13_Satai_Price
                            break
                        if list == ['11', '1']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room3_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room13_Satai_Price
                            break
                        if list == ['11', '2']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room3_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room13_Satai_Price
                            break
                        if list == ['11', '3']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room3_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room13_Satai_Price
                            break
                        if list == ['11', '4']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room3_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room3_Satai_Price
                            break
                        if list == ['11', '5']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room13_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room13_Satai_Price
                            break
                        if list == ['11', '6']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room34_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room34_Satai_Price
                            break
                        if list == ['11', '7']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room134_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room134_Satai_Price
                            break
                        if list == ['11', '8']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room134_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room134_Satai_Price
                            break
                        if list == ['12', '']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room12_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room12_Satai_Price
                            break
                        if list == ['12', '0']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room12_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room12_Satai_Price
                            break
                        if list == ['12', '1']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room12_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room12_Satai_Price
                            break
                        if list == ['12', '2']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room12_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room12_Satai_Price
                            break
                        if list == ['12', '3']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room12_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room12_Satai_Price
                            break
                        if list == ['12', '4']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room12_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room12_Satai_Price
                            break
                        if list == ['12', '5']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room12_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room12_Satai_Price
                            break
                        if list == ['12', '6']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room14_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room14_Satai_Price
                            break
                        if list == ['12', '7']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room1234_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room1234_Satai_Price
                            break
                        if list == ['12', '8']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room234_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room234_Satai_Price
                            break
                        if list == ['13', '']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room234_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room234_Satai_Price
                            break
                        if list == ['13', '0']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room234_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room234_Satai_Price
                            break
                        if list == ['13', '1']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room234_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room234_Satai_Price
                            break
                        if list == ['13', '2']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room234_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room234_Satai_Price
                            break
                        if list == ['13', '3']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room234_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room234_Satai_Price
                            break
                        if list == ['13', '4']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room234_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room234_Satai_Price
                            break
                        if list == ['13', '5']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room234_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room234_Satai_Price
                            break
                        if list == ['13', '6']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room1234_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room1234_Satai_Price
                            break
                        if list == ['13', '7']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room1234_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room1234_Satai_Price
                            break
                        if list == ['13', '8']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room1234_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room1234_Satai_Price
                            break
                        if list == ['14', '']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room1234_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room1234_Satai_Price
                            break
                        if list == ['14', '0']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room1234_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room1234_Satai_Price
                            break
                        if list == ['14', '1']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room1234_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room1234_Satai_Price
                            break
                        if list == ['14', '2']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room1234_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room1234_Satai_Price
                            break
                        if list == ['14', '3']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room1234_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room1234_Satai_Price
                            break
                        if list == ['14', '4']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room1234_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room1234_Satai_Price
                            break
                        if list == ['14', '5']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room1234_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room1234_Satai_Price
                            break
                        if list == ['14', '6']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room1234_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room1234_Satai_Price
                            break
                        if list == ['14', '7']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room1234_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room1234_Satai_Price
                            break
                        if list == ['14', '8']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room1234_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room1234_Satai_Price
                            break
                        if list == ['14', '1']:
                            print(Room1234_Iris_Definition + Hotel_Text + Room1234_Satai_Definition); list_Room_Price = Room1234_Iris_Price + Room1234_Satai_Price
                            break
                        # else:
                        #     print("Your Request Exceed Our Room Capacity Or you Entered Invalid Value")

            Room_Approval = input("Do you Approve Our Recommendation? Y/N\n").lower().lower()
            if Room_Approval == "y":
                Total_Price = (Choice_Days * list_Room_Price)
                print("Your total Price for " + str(Choice_Days) + " Days is " + str(Total_Price))
                sleep(S1)
                input_Confirmation = input("\n\nDo You confirm The Order? Y/N\n").lower()
                if input_Confirmation == "y":
                    Random_Number = random.randint(10000, 99999)
                    Order_Number = (First_Name + str(Random_Number))

                    print("\nYour Order received, your Order Number is: " + Order_Number)
                    file = open("D:\\" + Order_Number + ".txt", "w+")
                    file.close()
                    file = open("D:\\" + Order_Number + ".txt", "a")
                    file.write("Your Order Information is:"
                               "\n\n\n    Order Number:" + str(Order_Number) +
                               "\n    Full Name is: " + First_Name + " " + Last_Name +
                               "\n    Number of Adults: " + Adults_Number +
                               "\n    Number of Children: " + Children_Number +
                               "\n    Days of Stay: " + str(Choice_Days) +
                               # "\n    Hotel Name: "
                               # "\n    Room Description: "
                               "\n*************************************\n\n")
                    file.close()

                    sleep(S1)
                    Save_to_File = input("\nDo you want to save to file (PDF)? Y/N\n").lower()
                    if Save_to_File == "y":
                        pdf = FPDF()
                        pdf.add_page()
                        pdf.set_font("Arial", size=12)
                        pdf.cell(200, 10, txt="Order Number :" + Order_Number, ln=1, align="C")
                        pdf.cell(200, 15, txt="Your Name :" + First_Name + ", " + Last_Name, ln=1, align="C")
                        pdf.cell(200, 25, txt="Number of Adults: " + Adults_Number, ln=1, align="C")
                        pdf.cell(200, 30, txt="Number of Children: " + Children_Number, ln=1, align="C")
                        # pdf.cell(200, 20, txt="Room Order: " + Room_Approval, ln=1, align="C")
                        # pdf.cell(200, 35, txt="Hotel Name:  " + str(Choice_Hotel), ln=1, align="C")
                        pdf.cell(200, 40, txt="Number of Days:  " + str(Choice_Days), ln=1, align="C")
                        pdf.cell(200, 45, txt="Price:  " + str(Total_Price), ln=1, align="C")
                        pdf.output("d:\\"+Order_Number+".pdf")
                        os.startfile(r"d:\\"+Order_Number+".pdf")
                    if Save_to_File == "n":
                        continue

            if Room_Approval == "n":
                continue


        if choice == "3":           ## List Orders and Cancel Order
            print("Print All Orders....")
            path = 'D:\\'
            Order_Files = os.listdir(path)
            Order_Files_TXT = [i for i in Order_Files if i.endswith('.txt')]
            print(Order_Files_TXT)
            sleep(S1)
            Delete_File_Order = input("Do you want to remove on order? Y/N\n").lower()
            if Delete_File_Order == "y":
                path = 'D:\\'
                remove_file = input("Enter file name: ")
                os.remove(path + remove_file)
                print(remove_file, "File Removed!")


        if choice == "4":           ## Find Available Room
            Choice_Available_Setai = input("Print all days the rooms in Setai Hotel are Available? Y/N\n")
            if Choice_Available_Setai == "y":
                if Room1_Setai_Hotel['Sunday'] == 1: print("Room1 is Available on Sunday")
                if Room1_Setai_Hotel['Monday'] == 1: print("Room1 is Available on Monday")
                if Room1_Setai_Hotel['Tuesday'] == 1: print("Room1 is Available on Tuesday")
                if Room1_Setai_Hotel['Wednesday'] == 1: print("Room1 is Available on Wednesday")
                if Room1_Setai_Hotel['Thursday'] == 1: print("Room1 is Available on Thursday")

                if Room2_Setai_Hotel['Sunday'] == 1: print("Room2 is Available on Sunday")
                if Room2_Setai_Hotel['Monday'] == 1: print("Room2 is Available on Monday")
                if Room2_Setai_Hotel['Tuesday'] == 1: print("Room2 is Available on Tuesday")
                if Room2_Setai_Hotel['Wednesday'] == 1: print("Room2 is Available on Wednesday")
                if Room2_Setai_Hotel['Thursday'] == 1: print("Room2 is Available on Thursday")

                if Room3_Setai_Hotel['Sunday'] == 1: print("Room3 is Available on Sunday")
                if Room3_Setai_Hotel['Monday'] == 1: print("Room3 is Available on Monday")
                if Room3_Setai_Hotel['Tuesday'] == 1: print("Room3 is Available on Tuesday")
                if Room3_Setai_Hotel['Wednesday'] == 1: print("Room3 is Available on Wednesday")
                if Room3_Setai_Hotel['Thursday'] == 1: print("Room3 is Available on Thursday")

                if Room4_Setai_Hotel['Sunday'] == 1: print("Room4 is Available on Sunday")
                if Room4_Setai_Hotel['Monday'] == 1: print("Room4 is Available on Monday")
                if Room4_Setai_Hotel['Tuesday'] == 1: print("Room4 is Available on Tuesday")
                if Room4_Setai_Hotel['Wednesday'] == 1: print("Room4 is Available on Wednesday")
                if Room4_Setai_Hotel['Thursday'] == 1: print("Room4 is Available on Thursday")

            Choice_Available_Iris = input("Print all days the rooms in Iris Hotel are Available? Y/N\n")
            if Choice_Available_Iris == "y":
                if Room1_Iris_Hotel['Sunday'] == 1: print("Room1 is Available on Sunday")
                if Room1_Iris_Hotel['Monday'] == 1: print("Room1 is Available on Monday")
                if Room1_Iris_Hotel['Tuesday'] == 1: print("Room1 is Available on Tuesday")
                if Room1_Iris_Hotel['Wednesday'] == 1: print("Room1 is Available on Wednesday")
                if Room1_Iris_Hotel['Thursday'] == 1: print("Room1 is Available on Thursday")

                if Room2_Iris_Hotel['Sunday'] == 1: print("Room2 is Available on Sunday")
                if Room2_Iris_Hotel['Monday'] == 1: print("Room2 is Available on Monday")
                if Room2_Iris_Hotel['Tuesday'] == 1: print("Room2 is Available on Tuesday")
                if Room2_Iris_Hotel['Wednesday'] == 1: print("Room2 is Available on Wednesday")
                if Room2_Iris_Hotel['Thursday'] == 1: print("Room2 is Available on Thursday")

                if Room3_Iris_Hotel['Sunday'] == 1: print("Room3 is Available on Sunday")
                if Room3_Iris_Hotel['Monday'] == 1: print("Room3 is Available on Monday")
                if Room3_Iris_Hotel['Tuesday'] == 1: print("Room3 is Available on Tuesday")
                if Room3_Iris_Hotel['Wednesday'] == 1: print("Room3 is Available on Wednesday")
                if Room3_Iris_Hotel['Thursday'] == 1: print("Room3 is Available on Thursday")

                if Room4_Iris_Hotel['Sunday'] == 1: print("Room4 is Available on Sunday")
                if Room4_Iris_Hotel['Monday'] == 1: print("Room4 is Available on Monday")
                if Room4_Iris_Hotel['Tuesday'] == 1: print("Room4 is Available on Tuesday")
                if Room4_Iris_Hotel['Wednesday'] == 1: print("Room4 is Available on Wednesday")
                if Room4_Iris_Hotel['Thursday'] == 1: print("Room4 is Available on Thursday")



        if choice == "5":          ## Exit This Program
            choiceYN = input("Are You Sure? Y/N \n").lower()
            if choiceYN == "y":
                os.system('cls')
                print("Exiting the System...")
                sleep(S1)
                os.system('cls')
                break

            if choiceYN == "n":
                print("Welcome Back......")
                sleep(S1)
                os.system('cls')
                continue

            else:
                print("-- You Can Only Select Y/N --")
                sleep(S1)
                os.system('cls')
                continue

        # else:
        #     print("-- You Can Only Select 1-5 --")
        #     sleep(S1)
        #     os.system('cls')

###########      Rooms Definition      ################
Room1_Satai_Definition = '''
####################
#                  #
#   Room 1         #
#                  #
#   1 Adults       #
#   1 Children     #
#   OR             #
#   2 Adults       #
#                  #
#   Price:  300    #
#################### 
'''
Room2_Satai_Definition = '''
####################
#                  #
#   Room 2         #
#                  #
#   2 Adults       #
#   1 Children     #
#                  #
#   Price:  450    #
#################### 
'''
Room3_Satai_Definition = '''
####################
#                  #
#   Room 3         #
#                  #
#   3 Adults       #
#                  #
#                  #
#   Price:  550    #
#################### 
'''
Room4_Satai_Definition = '''
####################
#                  #
#   Room 4         #
#                  #
#   2 Adults       #
#   2 Children     #
#                  #
#   Price:  600    #
#################### 
'''

Room12_Satai_Definition = '''
####################    ####################  
#                  #    #                  # 
#   Room 1         #    #   Room 2         #  
#                  #    #                  # 
#   1 Adults       #    #   2 Adults       #  
#   1 Children     #    #   1 Children     #  
#   OR             #    #                  #  
#   2 Adults       #    #   Price:  450    # 
#                  #    ####################   
#   Price:  300    #
#################### 
'''
Room13_Satai_Definition = '''
####################    ####################  
#                  #    #                  #  
#   Room 1         #    #   Room 3         #  
#                  #    #                  #  
#   1 Adults       #    #   3 Adults       #  
#   1 Children     #    #                  #  
#   OR             #    #   Price:  550    #  
#   2 Adults       #    ####################  
#                  #                             
#   Price:  300    #
#################### 
'''
Room14_Satai_Definition = '''
####################    ####################
#                  #    #                  #
#   Room 1         #    #   Room 4         #
#                  #    #                  #
#   1 Adults       #    #   2 Adults       #
#   1 Children     #    #   2 Children     #
#   OR             #    #                  #
#   2 Adults       #    #   Price:  600    # 
#                  #    #################### 
#   Price:  300    #
#################### 
'''
Room23_Satai_Definition = '''
####################    #################### 
#                  #    #                  #  
#   Room 2         #    #   Room 3         #   
#                  #    #                  #  
#   2 Adults       #    #   3 Adults       #  
#   1 Children     #    #                  # 
#                  #    #   Price:  550    #  
#   Price:  450    #    ####################  
####################                         
'''
Room24_Satai_Definition = '''
####################    ####################
#                  #    #                  #
#   Room 2         #    #   Room 4         #
#                  #    #                  #
#   2 Adults       #    #   2 Adults       #
#   1 Children     #    #   2 Children     #
#                  #    #                  #
#   Price:  450    #    #   Price:  600    # 
####################    #################### 
'''
Room34_Satai_Definition = '''
####################    ####################
#                  #    #                  #
#   Room 3         #    #   Room 4         #
#                  #    #                  #
#   3 Adults       #    #   2 Adults       #
#                  #    #   2 Children     #
#   Price:  550    #    #                  #
####################    #   Price:  600    # 
                        #################### 
'''
Room123_Satai_Definition = '''
####################    ####################    ####################
#                  #    #                  #    #                  #
#   Room 1         #    #   Room 2         #    #   Room 3         #
#                  #    #                  #    #                  #
#   1 Adults       #    #   2 Adults       #    #   3 Adults       #
#   1 Children     #    #   1 Children     #    #                  #
#   OR             #    #                  #    #   Price:  550    #
#   2 Adults       #    #   Price:  450    #    ####################
#                  #    ####################                           
#   Price:  300    #
#################### 
'''
Room124_Satai_Definition = '''
####################    #####################   #####################
#                  #    #                   #   #                   #
#   Room 1         #    #   Room 2          #   #   Room 4          #
#                  #    #                   #   #                   #
#   1 Adults       #    #   2 Adults        #   #   2 Adults        #
#   1 Children     #    #   1 Children      #   #   2 Children      #
#   OR             #    #                   #   #                   #
#   2 Adults       #    #   Price:  450     #   #   Price:  600     #
#                  #    #####################   #####################                      
#   Price:  300    #
#################### 
'''
Room134_Satai_Definition = '''
####################    #####################   #####################
#                  #    #                   #   #                   #
#   Room 1         #    #   Room 3          #   #   Room 4          #
#                  #    #                   #   #                   #
#   1 Adults       #    #   3 Adults        #   #   2 Adults        #
#   1 Children     #    #                   #   #   2 Children      #
#   OR             #    #   Price:  450     #   #                   #
#   2 Adults       #    #####################   #   Price:  600     #
#                  #                            #####################                      
#   Price:  300    #
#################### 
'''
Room234_Satai_Definition = '''
####################    ####################    ####################
#                  #    #                  #    #                  #
#   Room 2         #    #   Room 3         #    #   Room 4         #
#                  #    #                  #    #                  #
#   2 Adults       #    #   3 Adults       #    #   2 Adults       #
#   1 Children     #    #                  #    #   2 Children     #
#                  #    #   Price:  550    #    #                  #
#   Price:  450    #    ####################    #   Price:  600    # 
####################                            #################### 
'''
Room1234_Satai_Definition = '''
***********************    Hotel Satai Rooms Listing  **************************************

####################    ####################    ####################    ####################
#                  #    #                  #    #                  #    #                  #
#   Room 1         #    #   Room 2         #    #   Room 3         #    #   Room 4         #
#                  #    #                  #    #                  #    #                  #
#   1 Adults       #    #   2 Adults       #    #   3 Adults       #    #   2 Adults       #
#   1 Children     #    #   1 Children     #    #                  #    #   2 Children     #
#   OR             #    #                  #    #   Price:  550    #    #                  #
#   2 Adults       #    #   Price:  450    #    ####################    #   Price:  600    # 
#                  #    ####################                            #################### 
#   Price:  300    #
#################### 
'''

Room1_Iris_Definition = '''
####################
#                  #
#   Room 1         #
#                  #
#   1 Adults       #
#   1 Children     #
#   OR             #
#   2 Adults       #
#                  #
#   Price:  200    #
#################### 
'''
Room2_Iris_Definition = '''
#####################
#                   #
#   Room 2          #
#                   #
#   2 Adults        #
#   1 Children      #
#                   #
#    Price:  250    #
##################### 
'''
Room3_Iris_Definition = '''
#####################
#                   #
#   Room 3          #
#                   #
#   3 Adults        #
#                   #
#                   #
#    Price:  350    #
##################### 
'''
Room4_Iris_Definition = '''
#####################
#                   #
#   Room 4          #
#                   #
#   2 Adults        #
#   2 Children      #
#                   #
#   Price:  450     #
##################### 
'''

Room12_Iris_Definition = '''
####################    #####################
#                  #    #                   #
#   Room 1         #    #   Room 2          #
#                  #    #                   #
#   1 Adults       #    #   2 Adults        #
#   1 Children     #    #   1 Children      # 
#   OR             #    #                   # 
#   2 Adults       #    #   Price:  250     # 
#                  #    ##################### 
#   Price:  200    #
#################### 
'''
Room13_Iris_Definition = '''
####################    #####################  
#                  #    #                   #  
#   Room 1         #    #   Room 3          #  
#                  #    #                   # 
#   1 Adults       #    #   3 Adults        # 
#   1 Children     #    #                   #  
#   OR             #    #   Price:  350     #  
#   2 Adults       #    ##################### 
#                  #                            
#   Price:  200    #
#################### 
'''
Room14_Iris_Definition = '''
####################    #####################
#                  #    #                   #
#   Room 1         #    #   Room 4          #
#                  #    #                   #
#   1 Adults       #    #   2 Adults        #
#   1 Children     #    #   2 Children      #
#   OR             #    #                   #
#   2 Adults       #    #   Price:  450     #
#                  #    #####################
#   Price:  200    #
#################### 
'''
Room23_Iris_Definition = '''
#####################   ##################### 
#                   #   #                   # 
#   Room 2          #   #   Room 3          # 
#                   #   #                   #  
#   2 Adults        #   #   3 Adults        #  
#   1 Children      #   #                   #  
#                   #   #   Price:  350     # 
#   Price:  250     #   ##################### 
#####################                         
'''
Room24_Iris_Definition = '''
#####################   #####################
#                   #   #                   #
#   Room 2          #   #   Room 4          #
#                   #   #                   #
#   2 Adults        #   #   2 Adults        #
#   1 Children      #   #   2 Children      #
#                   #   #                   #
#   Price:  250     #   #   Price:  450     #
#####################   #####################
'''
Room34_Iris_Definition = '''
#####################   #####################
#                   #   #                   #
#   Room 3          #   #   Room 4          #
#                   #   #                   #
#   3 Adults        #   #   2 Adults        #
#                   #   #   2 Children      #
#   Price:  350     #   #                   #
#####################   #   Price:  450     #
                        #####################
'''
Room123_Iris_Definition = '''
####################    #####################   #####################
#                  #    #                   #   #                   #
#   Room 1         #    #   Room 2          #   #   Room 3          #
#                  #    #                   #   #                   #
#   1 Adults       #    #   2 Adults        #   #   3 Adults        #
#   1 Children     #    #   1 Children      #   #                   #
#   OR             #    #                   #   #   Price:  350     #
#   2 Adults       #    #   Price:  250     #   #####################
#                  #    #####################                         
#   Price:  200    #
#################### 
'''
Room124_Iris_Definition = '''
####################    #####################   #####################
#                  #    #                   #   #                   #
#   Room 1         #    #   Room 2          #   #   Room 4          #
#                  #    #                   #   #                   #
#   1 Adults       #    #   2 Adults        #   #   2 Adults        #
#   1 Children     #    #   1 Children      #   #   2 Children      #
#   OR             #    #                   #   #                   #
#   2 Adults       #    #   Price:  250     #   #   Price:  450     #
#                  #    #####################   #####################                      
#   Price:  200    #
#################### 
'''
Room134_Iris_Definition = '''
####################    #####################   #####################
#                  #    #                   #   #                   #
#   Room 1         #    #   Room 3          #   #   Room 4          #
#                  #    #                   #   #                   #
#   1 Adults       #    #   3 Adults        #   #   2 Adults        #
#   1 Children     #    #                   #   #   2 Children      #
#   OR             #    #   Price:  250     #   #                   #
#   2 Adults       #    #####################   #   Price:  450     #
#                  #                            #####################                      
#   Price:  200    #
#################### 
'''
Room234_Iris_Definition = '''
#####################   #####################   #####################
#                   #   #                   #   #                   #
#   Room 2          #   #   Room 3          #   #   Room 4          #
#                   #   #                   #   #                   #
#   2 Adults        #   #   3 Adults        #   #   2 Adults        #
#   1 Children      #   #                   #   #   2 Children      #
#                   #   #   Price:  350     #   #                   #
#   Price:  250     #   #####################   #   Price:  450     #
#####################                           #####################
'''
Room1234_Iris_Definition = '''
***********************    Hotel Iris Rooms Listing  ****************************************

####################    #####################   #####################   #####################
#                  #    #                   #   #                   #   #                   #
#   Room 1         #    #   Room 2          #   #   Room 3          #   #   Room 4          #
#                  #    #                   #   #                   #   #                   #
#   1 Adults       #    #   2 Adults        #   #   3 Adults        #   #   2 Adults        #
#   1 Children     #    #   1 Children      #   #                   #   #   2 Children      #
#   OR             #    #                   #   #   Price:  350     #   #                   #
#   2 Adults       #    #   Price:  250     #   #####################   #   Price:  450     #
#                  #    #####################                           #####################
#   Price:  200    #
#################### 
'''

###########      Rooms Price Definition      ################
Room1_Satai_Price = Room1_Satai_Definition
Room2_Satai_Price = Room2_Satai_Definition
Room3_Satai_Price = Room2_Satai_Definition
Room4_Satai_Price = Room2_Satai_Definition

Room1_Satai_Price = 300
Room2_Satai_Price = 450
Room3_Satai_Price = 550
Room4_Satai_Price = 600

Room12_Satai_Price = Room1_Satai_Price + Room2_Satai_Price
Room13_Satai_Price = Room1_Satai_Price + Room3_Satai_Price
Room14_Satai_Price = Room1_Satai_Price + Room4_Satai_Price
Room23_Satai_Price = Room2_Satai_Price + Room3_Satai_Price
Room24_Satai_Price = Room2_Satai_Price + Room4_Satai_Price
Room34_Satai_Price = Room3_Satai_Price + Room4_Satai_Price
Room123_Satai_Price = Room1_Satai_Price + Room2_Satai_Price + Room3_Satai_Price
Room124_Satai_Price = Room1_Satai_Price + Room2_Satai_Price + Room4_Satai_Price
Room134_Satai_Price = Room1_Satai_Price + Room3_Satai_Price + Room4_Satai_Price
Room234_Satai_Price = Room2_Satai_Price + Room3_Satai_Price + Room4_Satai_Price
Room1234_Satai_Price = Room1_Satai_Price + Room2_Satai_Price + Room3_Satai_Price + Room4_Satai_Price

Room1_Iris_Price = Room1_Iris_Definition
Room2_Iris_Price = Room2_Iris_Definition
Room3_Iris_Price = Room2_Iris_Definition
Room4_Iris_Price = Room2_Iris_Definition

Room1_Iris_Price = 200
Room2_Iris_Price = 250
Room3_Iris_Price = 350
Room4_Iris_Price = 450

Room12_Iris_Price = Room1_Iris_Price + Room2_Iris_Price
Room13_Iris_Price = Room1_Iris_Price + Room3_Iris_Price
Room14_Iris_Price = Room1_Iris_Price + Room4_Iris_Price
Room23_Iris_Price = Room2_Iris_Price + Room3_Iris_Price
Room24_Iris_Price = Room2_Iris_Price + Room4_Iris_Price
Room34_Iris_Price = Room3_Iris_Price + Room4_Iris_Price
Room123_Iris_Price = Room1_Iris_Price + Room2_Iris_Price + Room3_Iris_Price
Room124_Iris_Price = Room1_Iris_Price + Room2_Iris_Price + Room4_Iris_Price
Room134_Iris_Price = Room1_Iris_Price + Room3_Iris_Price + Room4_Iris_Price
Room234_Iris_Price = Room2_Iris_Price + Room3_Iris_Price + Room4_Iris_Price
Room1234_Iris_Price = Room1_Iris_Price + Room2_Iris_Price + Room3_Iris_Price + Room4_Iris_Price


Menu()
