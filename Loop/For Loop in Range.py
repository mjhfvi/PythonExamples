'''
For Loop in Range
'''

dict_dog={}
for x in range(3):
    dict_dog[input("Enter dog name: ")] = (7*int(input("Enter dog age: ")))

print(str(dict_dog))