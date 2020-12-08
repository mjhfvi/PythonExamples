import json

######################  File Path  ####################################################
FolderRootPath = "D:\\HotelProject\\"
FileOrdersPath = "Orders.json"
############  Testing for an Existing Folder ##########################################
FromFile = (FolderRootPath + FileOrdersPath)

jsonFile = open(FromFile, 'r')
json_object = json.load(jsonFile)
jsonFile.close()
print(json_object['Order']['FirstName'])

json_object['Order']["FirstName"] = "Tzahi2"
with open(FromFile, 'w') as jsonFile:
    json.dump(json_object, jsonFile)
    jsonFile.close()

print("\nPrint FirstName after the update")
print(json_object['Order']['FirstName'])
