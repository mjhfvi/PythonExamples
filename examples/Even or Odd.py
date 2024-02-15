'''
Write a Python program to find whether a number (accept from the user) is even or odd,
print out an appropriate message to the user.

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))


   Source: https://www.programiz.com/python-programming/examples/odd-even
'''

number=int(input("Please input your Number: "))
if (number % 2 == 0):
    print("{0} is Even".format(number))

else:
    print("{0} is Odd".format(number))

