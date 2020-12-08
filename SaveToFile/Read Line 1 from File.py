import os
inputUserSelect = {'OrderNumber': 10000, 'OrderActive': 0, 'FirstName': 0, 'LastName': 0, 'AdultsNumber': 0, 'DaySelect': 0}
# os.mkdir(FolderRootPath)
FolderRootPath = "D:\\HotelProject\\"
FileOrdersPath = "Orders.txt"

FromFile = (FolderRootPath + FileOrdersPath)
with open(FromFile) as fp:
    line = fp.readline()

print(line)