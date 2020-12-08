import json

file_name = "D:\\ComputerList.json"

# ### Stage 1, input first time get input from user and update dictionary
host_input = input('Enter Host Name: ')
ip_input = input('Enter IP Address: ')
user_input = input('Enter User Name: ')
password_input = input('Enter User Password: ')

# dictionary = {'0':{'host':host_input, 'ip':ip_input, 'user':user_input, 'password':password_input}}
dictionary = {'0':{'host':'host', 'ip':'ip', 'user':'user', 'password':'password'}}

# ### Stage 1, input first time Write to File
json_file = open(file_name, "w")
json.dump(dictionary, json_file, indent=4)
json_file.close()

# ### Stage 1, Load from File
json_file = open(file_name, 'r')
json_object = json.load(json_file)
json_file.close()

# ### Stage 1, Print Load Data
print('\n#########  Printing only index 00  ##########')
print(json_object)
print('Dictionary Type is: ', type(json_object))
print('\n')

# ### Stage 2, Get Index Information
for x in dictionary:
    index = int(x)
    print(int(index))
    print(type(index))
    item = (index + 1)
    print(item)
    print(type(item))

# ### Stage 2, Update dictionary with a dictionary
host_input = input('Enter Host Name: ')
ip_input = input('Enter IP Address: ')
user_input = input('Enter User Name: ')
password_input = input('Enter User Password: ')

# ### Stage 2, Update Dictionary Information and Index Number
dictionary_add = {item:{'host':host_input, 'ip':ip_input, 'user':user_input, 'password':password_input}}

dictionary.update(dictionary_add)
print(dictionary)
print('Dictionary Type is: ', type(dictionary))

# ### Stage 2, Write to File
json_file = open(file_name, "w")
json.dump(dictionary, json_file, indent=4)
json_file.close()

# ### Stage 2, Load from File
json_file = open(file_name, 'r')
json_object = json.load(json_file)
json_file.close()

# ### Stage 2, Print Load Data
print('\n#########  Printing only index 00  ##########')
print(json_object)
print('Dictionary Type is: ', type(json_object))
print('\n')

# ### Stage 3, Get Index Information
# count = 0
# for x in object:
#     if isinstance(object[x], dict):
#         count += len(object[x])

# ### Stage 3, Update dictionary with a dictionary
host_input = input('Enter Host Name: ')
ip_input = input('Enter IP Address: ')
user_input = input('Enter User Name: ')
password_input = input('Enter User Password: ')

# ### Stage 3, Update Dictionary Information and Index Number
dictionary_add = {item:{'host':host_input, 'ip':ip_input, 'user':user_input, 'password':password_input}}

dictionary.update(dictionary_add)
print(dictionary)
print('Dictionary Type is: ', type(dictionary))

# ### Stage 3, Write Update to File
json_file = open(file_name, "w")
json.dump(dictionary, json_file, indent=4)
json_file.close()
