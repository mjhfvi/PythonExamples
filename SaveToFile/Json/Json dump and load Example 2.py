import json

######################  File Path  ####################################################
FolderRootPath = "D:\\HotelProject\\"
FileOrdersPath = "Orders.json"
############  Testing for an Existing Folder ##########################################
FromFile = (FolderRootPath + FileOrdersPath)

# Dictionary Information

dictionary = {"OrderInfo":{"OrderNumber":11111,"OrderActive":"true","AdultsNumber":3,"ChildrenNumber":4,},"UserInfo":{"FirstName":"Tzahi","LastName":"Cohen"},"HotelInfo":{"Satai":"false","Iris":"false"},"RoomInfo":{"Room1":"false","Room2":"false","Room3":"false","Room4":"false"},"DaysInfo":{"Sunday":"false","Monday":"false","Tuesday":"false","Wednesday":"false","Thursday":"false"}}


# Data to be written
with open(FromFile, 'w') as jsonFile:
    json.dump(dictionary, jsonFile, indent=4)
    jsonFile.close()

# Load File
json_file = open(FromFile, 'r')
json_object = json.load(json_file)
jsonFile.close()

# Print File
print('\nPrint OrderInfo of dictionary list\n\n', json_object['OrderInfo'])
print('\n###############################################################\n')
print('\nPrint UserInfo of dictionary list\n\n', json_object['UserInfo'])
print('\n###############################################################\n')
print('\nPrint HotelInfo of dictionary list\n\n', json_object['HotelInfo'])
print('\n###############################################################\n')
print('\nPrint RoomInfo of dictionary list\n\n', json_object['RoomInfo'])
print('\n###############################################################\n')
print('\nPrint DaysInfo of dictionary list\n\n', json_object['DaysInfo'])
print('\n###############################################################\n')





