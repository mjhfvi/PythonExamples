import json
######################  File Path  ##############################
FolderRootPath = "D:\\HotelProject\\"
FileOrdersPath = "Orders.json"

######################  Dictionary Info  ##############################
inputUserSelect = {}                                    ##### Master Dictionary
inputUserSelect['OrderConfirm'] = []                    ##### List1 Append
inputUserSelect['OrderConfirm'].append({'OrderNumber': '10000', 'OrderActive': '0',})

inputUserSelect['UserInfo'] = []                        ##### List2 Append
inputUserSelect['UserInfo'].append({'FirstName': '0',
                                    'LastName': '0',
                                    'AdultsNumber': '0',
                                    'ChildrenNumber': '0',})

inputUserSelect['HotelInfo'] = []                       ##### List3 Append
inputUserSelect['HotelInfo'].append({'HotelSelect': '0', 'DaySelect': '0'})

######################  Open Local File  ##############################
with open(FolderRootPath + FileOrdersPath, 'w') as outfile:
    json.dump(inputUserSelect, outfile)

######################  Print Info From File  ##########################
with open(FolderRootPath + FileOrdersPath) as json_file:
    inputUserSelect = json.load(json_file)
    for p in inputUserSelect['UserInfo']:
        print('FirstName: ' + p['FirstName'])
        print('LastName: ' + p['LastName'])
        print('AdultsNumber: ' + p['AdultsNumber'])
        print('ChildrenNumber: ' + p['ChildrenNumber'])
    for i in inputUserSelect['HotelInfo']:
        print('HotelSelect: ' + i['HotelSelect'])
        print('DaySelect: ' + i['DaySelect'])
    for u in inputUserSelect['OrderConfirm']:
        print('OrderNumber: ' + u['OrderNumber'])
        print('OrderActive: ' + u['OrderActive'])

########################################################################################
########################  Append New Line To File  #####################################
########################################################################################
from Definition_Room import *
import json
######################  File Path  ##############################
FolderRootPath = "D:\\HotelProject\\"
FileOrdersPath = "Orders.json"
FileDefinitionPath = "Definition.json"


with open(FolderRootPath + FileDefinitionPath, 'w') as outfile:
    json.dump(Room1_Setai_Hotel, outfile); outfile.write("\n")
    json.dump(Room2_Setai_Hotel, outfile); outfile.write("\n")
    json.dump(Room3_Setai_Hotel, outfile); outfile.write("\n")
    json.dump(Room4_Setai_Hotel, outfile); outfile.write("\n")
    json.dump(Room1_Iris_Hotel , outfile); outfile.write("\n")
    json.dump(Room2_Iris_Hotel, outfile); outfile.write("\n")
    json.dump(Room3_Iris_Hotel, outfile); outfile.write("\n")
    json.dump(Room4_Iris_Hotel, outfile); outfile.write("\n")
    outfile.close()
