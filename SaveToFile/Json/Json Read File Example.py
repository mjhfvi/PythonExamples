import json

######################  File Path  ####################################################
FolderRootPath = "D:\\HotelProject\\"
FileOrdersPath = "Orders.json"
############  Testing for an Existing Folder ##########################################
FromFile = (FolderRootPath + FileOrdersPath)

# Opening JSON file
with open(FromFile, "r") as json_file:
    data = json.load(json_file)
    print('\n\n##############################################################################################################')
    print(data['OrderInfo'])
    print(data['UserInfo'])
    print(data['Hotel'])
    print(data['Rooms'])
    print(data['Days'])
    print('##############################################################################################################\n\n')

with open(FromFile, "r") as json_file:
    inputUserSelect = json.load(json_file)
    for oi in inputUserSelect['OrderInfo']:
        print('\n\n##############################################################################################################')
        print('OrderNumber: ' + oi['OrderNumber'])
        print('OrderActive: ' + oi['OrderActive'])
        print('AdultsNumber: ' + oi['AdultsNumber'])
        print('ChildrenNumber: ' + oi['ChildrenNumber'])
    for ui in inputUserSelect['UserInfo']:
        print('FirstName: ' + ui['FirstName'])
        print('LastName: ' + ui['LastName'])
    for h in inputUserSelect['Hotel']:
        print('Satai: ' + h['Satai'])
        print('Iris: ' + h['Iris'])
    for r in inputUserSelect['Rooms']:
        print('Room1: ' + r['Room1'])
        print('Room2: ' + r['Room2'])
        print('Room3: ' + r['Room3'])
        print('Room4: ' + r['Room4'])
    for d in inputUserSelect['Days']:
        print('Sunday: ' + d['Sunday'])
        print('Monday: ' + d['Monday'])
        print('Tuesday: ' + d['Tuesday'])
        print('Wednesday: ' + d['Wednesday'])
        print('Thursday: ' + d['Thursday'])
        print('##############################################################################################################\n\n')
    json_file.close()

