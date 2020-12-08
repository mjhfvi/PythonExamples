# Main Car List
carlist = ["Ford","Kia","Hyundai","Honda","Jeep"]

# Print List and Number
print("Your List of Cars : " + str(carlist) + "\nyour list length is :" + str(len(carlist)))

# add more Cars to the List
carlistinput = [input("enter your first car name: "), input("enter your second car name: "), input("enter your third  car name: "), input("enter your fourth car name: ")]
carlist.append(carlistinput)

# Print new Cars to the old List
print("Your Old List of Cars : " + str(carlist) + "\nyour list length is :" + str(len(carlist)))

# Check if you have a Car in the carlist
# print("2" in [carlist])

# print(int(len(carlistinput)))
# print(pop1)
# pop1 = carlist.pop(0)