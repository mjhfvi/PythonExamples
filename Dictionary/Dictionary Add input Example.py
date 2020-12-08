thisdict = {"brand": "Ford","model": "Mustang","year": 1964}

item1 = input("Please input a key: ")
item2 = input("Please input a value: ")


if item1 in thisdict:
  print("Yes, " + item1 + " is one of the keys in the this dict dictionary")
  print(thisdict)
else:
  print("not in the list, we are adding it")
  thisdict.update({item1: item2})
print(thisdict)