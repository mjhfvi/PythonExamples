# Prints out 0,1,2,3,....100

# count = 1
# while count < 100:
#     print(count)
#     count += 1  # This is the same as count = count + 1


# for x in range(0, 11):
#     print("Number %d" % (x))

# i = 1
# while i < 10:
#     print(i)
#     if i == 2:
#         break
#     i += 1

# i = 0
# while i < 100:
#     i += 1
#     if i == 5:
#         continue
#     print(i)


choice=input("Menu:\n1. 1-100:\n2. list fibo:\nEnter your choice:")
if choice=="1":
    for i in range(101):
        print(i)
    elif choice="2":
        fibo = [1, 2, 3, 5, 8, 13, 21]
        # 0 1 2 3 4 5 6
        boolean = "True"
        # for i in range (2,7):

        for i range(2, len(fibo)):
            print(fibo[i])
            print(fibo[i - 1])
            print(fibo[i - 2])
            if fibo[i] == (fibo[i - 1] + fibo[i - 2]):
                continue
            else:
                boolean = "False"
                break
        if boolean == "True"


input ("do you wany to quit yes/no:")
