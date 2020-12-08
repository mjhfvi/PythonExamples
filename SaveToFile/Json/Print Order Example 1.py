import json

FolderRootPath = "D:\\HotelProject\\"
FileOrdersPath = "Orders.json"
FromFile = (FolderRootPath + FileOrdersPath)

Order1001 = {'OrderNumber':'1001', 'OrderActive':'true', 'OrderInfo':{'UserInfo': {"FirstName": "Tzahi", "LastName": "Cohen"},'Hotel':{'Satai':'false','Iris':'false'},'Rooms':{'Room1':'false', 'Room2':'false', 'Room3':'false', 'Room4':'false'},'Days':{'Sunday': 'false', 'Monday': 'false', 'Tuesday': 'false', 'Wednesday': 'false', 'Thursday': 'false'}}}
Order1002 = {'OrderNumber':'1002', 'OrderActive':'true', 'OrderInfo':{'UserInfo': {"FirstName": "Rza", "LastName": "Cohen"},'Hotel':{'Satai':'false','Iris':'false'},'Rooms':{'Room1':'false', 'Room2':'false', 'Room3':'false', 'Room4':'false'},'Days':{'Sunday': 'false', 'Monday': 'false', 'Tuesday': 'false', 'Wednesday': 'false', 'Thursday': 'false'}}}
Order1003 = {'OrderNumber':'1003', 'OrderActive':'true', 'OrderInfo':{'UserInfo': {"FirstName": "Poal", "LastName": "Cohen"},'Hotel':{'Satai':'false','Iris':'false'},'Rooms':{'Room1':'false', 'Room2':'false', 'Room3':'false', 'Room4':'false'},'Days':{'Sunday': 'false', 'Monday': 'false', 'Tuesday': 'false', 'Wednesday': 'false', 'Thursday': 'false'}}}
Order1004 = {'OrderNumber':'1004', 'OrderActive':'true', 'OrderInfo':{'UserInfo': {"FirstName": "Orenay", "LastName": "Cohen"},'Hotel':{'Satai':'false','Iris':'false'},'Rooms':{'Room1':'false', 'Room2':'false', 'Room3':'false', 'Room4':'false'},'Days':{'Sunday': 'false', 'Monday': 'false', 'Tuesday': 'false', 'Wednesday': 'false', 'Thursday': 'false'}}}


OrderPrint = (Order1004)
print(OrderPrint['OrderInfo']['UserInfo']['FirstName'])
print(OrderPrint['OrderInfo']['Days']['Tuesday'])
print(OrderPrint['OrderInfo']['Rooms']['Room2'])

