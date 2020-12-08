import json

######################  File Path  ####################################################
FolderRootPath = "D:\\HotelProject\\"
FileOrdersPath = "Orders.json"
############  Testing for an Existing Folder ##########################################
FromFile = (FolderRootPath + FileOrdersPath)

json_file = open(FromFile, 'r')
json_object = json.load(json_file)
print("#######################################")
print(json_object)
print("#######################################")

json_object['OrderList']["0"]['UserInfo']['FirstName'] = "Tzahi"
json_object['OrderList']["0"]['UserInfo']['LastName'] = "Cohen"
json_object['OrderList']["0"]['OrderInfo']['OrderActive'] = "true"

with open(FromFile, 'r+') as jsonFile:
    json.dump(json_object, jsonFile, indent = 4)
    jsonFile.close()
print('##################################################################\n\n')
print(json_object)
print(json_object['OrderList']["0"]['OrderInfo'])
print(json_object['OrderList']["0"]['UserInfo'])





