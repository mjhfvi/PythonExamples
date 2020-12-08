import json

FolderRootPath = "D:\\HotelProject\\"
FileOrdersPath = "Orders.json"
FromFile = (FolderRootPath + FileOrdersPath)


Order1001 = {'OrderActive':'true', 'OrderInfo':{'OrderNumber':'1001', 'OrderActive':'true'}, 'UserInfo': {"FirstName": "Tzahi1", "LastName": "Cohen1"},'Hotel':{'Satai':'false','Iris':'false'},'Rooms':{'Room1':'false', 'Room2':'false', 'Room3':'false', 'Room4':'false'},'Days':{'Sunday': 'false', 'Monday': 'false', 'Tuesday': 'false', 'Wednesday': 'false', 'Thursday': 'false'}}
Order1002 = {'OrderActive':'true', 'OrderInfo':{'OrderNumber':'1002', 'OrderActive':'true'}, 'UserInfo': {"FirstName": "Tzahi1", "LastName": "Cohen1"},'Hotel':{'Satai':'false','Iris':'false'},'Rooms':{'Room1':'false', 'Room2':'false', 'Room3':'false', 'Room4':'false'},'Days':{'Sunday': 'false', 'Monday': 'false', 'Tuesday': 'false', 'Wednesday': 'false', 'Thursday': 'false'}}
Order1003 = {'OrderActive':'true', 'OrderInfo':{'OrderNumber':'1003', 'OrderActive':'true'}, 'UserInfo': {"FirstName": "Tzahi1", "LastName": "Cohen1"},'Hotel':{'Satai':'false','Iris':'false'},'Rooms':{'Room1':'false', 'Room2':'false', 'Room3':'false', 'Room4':'false'},'Days':{'Sunday': 'false', 'Monday': 'false', 'Tuesday': 'false', 'Wednesday': 'false', 'Thursday': 'false'}}
Order1004 = {'OrderActive':'true', 'OrderInfo':{'OrderNumber':'1004', 'OrderActive':'true'}, 'UserInfo': {"FirstName": "Tzahi1", "LastName": "Cohen1"},'Hotel':{'Satai':'false','Iris':'false'},'Rooms':{'Room1':'false', 'Room2':'false', 'Room3':'false', 'Room4':'false'},'Days':{'Sunday': 'false', 'Monday': 'false', 'Tuesday': 'false', 'Wednesday': 'false', 'Thursday': 'false'}}
Order1005 = {'OrderActive':'true', 'OrderInfo':{'OrderNumber':'1005', 'OrderActive':'true'}, 'UserInfo': {"FirstName": "Tzahi1", "LastName": "Cohen1"},'Hotel':{'Satai':'false','Iris':'false'},'Rooms':{'Room1':'false', 'Room2':'false', 'Room3':'false', 'Room4':'false'},'Days':{'Sunday': 'false', 'Monday': 'false', 'Tuesday': 'false', 'Wednesday': 'false', 'Thursday': 'false'}}


OrderPrint = (Order1005)
print(OrderPrint['OrderInfo'])
print(OrderPrint['UserInfo'])
print(OrderPrint['Days'])
print(OrderPrint['Rooms'])
print(OrderPrint['Hotel'])
