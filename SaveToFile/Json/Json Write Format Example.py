import json

######################  File Path  ####################################################
FolderRootPath = "D:\\HotelProject\\"
FileOrdersPath = "Orders.json"
############  Testing for an Existing Folder ##########################################
FromFile = (FolderRootPath + FileOrdersPath)

# Data to be written
dictionary = {
    'OrderInfo': [
        {
            'OrderNumber': 1002,
            'OrderActive': 'true',
            'AdultsNumber': 3,
            'ChildrenNumber': 4
        }
    ],
    'UserInfo': [
        {
            'FirstName': 'Tzahi',
            'LastName': 'Cohen'
        },
    ],
    'Hotel': [
        {
            'Satai': 'false',
            'Iris': 'false'
        },
    ],
    'Rooms': [
        {
            'Room1': 'false',
            'Room2': 'false',
            'Room3': 'false',
            'Room4': 'false'
        },
    ],
    'Days': [
        {
            'Sunday': 'false',
            'Monday': 'false',
            'Tuesday': 'false',
            'Wednesday': 'false',
            'Thursday': 'false'
        },
    ]
}


with open(FromFile, "w") as json_file:
    json.dump(dictionary, json_file)
    json_file.close()