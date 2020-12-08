list_Days_Stay = []
list_Choice_Hotel = []
list_Room_Choice = []

Choice_Hotel = input("Select the Hotel: \n"
                     "1. Hotel Setai \n"
                     "2. Hotel Iris \n")
if Choice_Hotel == "1":
    list_Choice_Hotel.append("Setai")

if Choice_Hotel == "2":
    list_Choice_Hotel.append("Iris")

Room1_Setai_Hotel = {'Sunday': 0, 'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0}
Room2_Setai_Hotel = {'Sunday': 0, 'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0}
Room3_Setai_Hotel = {'Sunday': 0, 'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0}
Room4_Setai_Hotel = {'Sunday': 0, 'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0}

Room1_Iris_Hotel = {'Sunday': 0, 'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0}
Room2_Iris_Hotel = {'Sunday': 0, 'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0}
Room3_Iris_Hotel = {'Sunday': 0, 'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0}
Room4_Iris_Hotel = {'Sunday': 0, 'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0}


inputStaySunday = input("Sunday: Y/N  ").lower()
if inputStaySunday == "y": list_Days_Stay.append("Sunday")
inputStayMonday = input("Monday: Y/N  ").lower()
if inputStayMonday == "y": list_Days_Stay.append("Monday")
inputStayTuesday = input("Tuesday: Y/N  ").lower()
if inputStayTuesday == "y": list_Days_Stay.append("Tuesday")
inputStayWednesday = input("Wednesday: Y/N  ").lower()
if inputStayWednesday == "y": list_Days_Stay.append("Wednesday")
inputStayThursday = input("Thursday: Y/N  ").lower()
if inputStayThursday == "y": list_Days_Stay.append("Thursday")

inputRoom = input("Select Room: \n"
                  "1. Room1\n"
                  "2. Room2\n"
                  "3. Room3\n")
if inputRoom == "1":
    list_Room_Choice.append('Room1')
if inputRoom == "2":
    list_Room_Choice.append('Room2')
if inputRoom == "3":
    list_Room_Choice.append('Room2')

print("###############################")

if "Setai" in list_Choice_Hotel:
    print("My Choice is Setai")
    if "Sunday" in list_Days_Stay:
        if Room1_Setai_Hotel['Sunday'] == 0: print("Room1 is Available on Sunday")
        if Room1_Setai_Hotel['Sunday'] == 1: print("Room1 is NOT Available on Sunday")

    if "Monday" in list_Days_Stay:
        if Room1_Setai_Hotel['Monday'] == 0: print("Room1 is Available on Monday")
        if Room1_Setai_Hotel['Monday'] == 1: print("Room1 is NOT Available on Monday")

    if "Tuesday" in list_Days_Stay:
        if Room1_Setai_Hotel['Tuesday'] == 0: print("Room1 is Available on Tuesday")
        if Room1_Setai_Hotel['Tuesday'] == 1: print("Room1 is NOT Available on Tuesday")

    if "Wednesday" in list_Days_Stay:
        if Room1_Setai_Hotel['Wednesday'] == 0: print("Room1 is Available on Wednesday")
        if Room1_Setai_Hotel['Wednesday'] == 1: print("Room1 is NOT Available on Wednesday")

    if "Thursday" in list_Days_Stay:
        if Room1_Setai_Hotel['Thursday'] == 0: print("Room1 is Available on Thursday")
        if Room1_Setai_Hotel['Thursday'] == 1: print("Room1 is NOT Available on Thursday")


if "Iris" in list_Choice_Hotel:
    print("My Choice is Iris")
    if "Sunday" in list_Days_Stay:
        if Room1_Iris_Hotel['Sunday'] == 0: print("Room1 is Available on Sunday")
        if Room1_Iris_Hotel['Sunday'] == 1: print("Room1 is NOT Available on Sunday")

    if "Monday" in list_Days_Stay:
        if Room1_Iris_Hotel['Monday'] == 0: print("Room1 is Available on Monday")
        if Room1_Iris_Hotel['Monday'] == 1: print("Room1 is NOT Available on Monday")

    if "Tuesday" in list_Days_Stay:
        if Room1_Iris_Hotel['Tuesday'] == 0: print("Room1 is Available on Tuesday")
        if Room1_Iris_Hotel['Tuesday'] == 1: print("Room1 is NOT Available on Tuesday")

    if "Wednesday" in list_Days_Stay:
        if Room1_Iris_Hotel['Wednesday'] == 0: print("Room1 is Available on Wednesday")
        if Room1_Iris_Hotel['Wednesday'] == 1: print("Room1 is NOT Available on Wednesday")

    if "Thursday" in list_Days_Stay:
        if Room1_Iris_Hotel['Thursday'] == 0: print("Room1 is Available on Thursday")
        if Room1_Iris_Hotel['Thursday'] == 1: print("Room1 is NOT Available on Thursday")

choice_change_Sunday = input("Sunday Y/N  ")
if choice_change_Sunday == "y":
    Room1_Setai_Hotel['Sunday'] = "1"
choice_change_Monday = input("Monday Y/N  ")
if choice_change_Monday == "y":
    Room1_Setai_Hotel['Monday'] = "1"
choice_change_Tuesday = input("Tuesday Y/N  ")
if choice_change_Tuesday == "y":
    Room1_Setai_Hotel['Tuesday'] = "1"
choice_change_Wednesday = input("Wednesday Y/N  ")
if choice_change_Wednesday == "y":
    Room1_Setai_Hotel['Wednesday'] = "1"
choice_change_Thursday = input("Thursday Y/N  ")
if choice_change_Thursday == "y":
    Room1_Setai_Hotel['Thursday'] = "1"


print("###################\n")
if list_Choice_Hotel == "Setai":
    print()
elif list_Room_Choice == "Room1":
    print()
elif 'Sunday' in list_Days_Stay:
    print("Setai Hotel, Room1 Available in Sunday")
print("###################\n")
if list_Choice_Hotel == "Setai":
    print()
elif 'Monday' in list_Days_Stay:
    print("Setai Hotel Available in Monday")
print("###################\n")
if list_Choice_Hotel == "Setai":
    print()
elif 'Tuesday' in list_Days_Stay:
    print("Setai Hotel Available in Tuesday")
print("###################\n")
if list_Choice_Hotel == "Setai":
    print()
elif 'Wednesday' in list_Days_Stay:
    print("Setai Hotel Available in Wednesday")
print("###################\n")
if list_Choice_Hotel == "Setai":
    print()
elif 'Thursday' in list_Days_Stay:
    print("Setai Hotel Available in Thursday")
print("###################\n")

print(list_Days_Stay)
print(list_Choice_Hotel)
print(list_Room_Choice)

print("###################\n")
print(Room1_Setai_Hotel)