print("enter your badget")
budget = int(input("what is your gudget? \n"))
facebook = int(input("enter how long is your facebook campagin: \n"))*100
instagram = int(input("how loan is your instgram compagin: \n"))*50
sum=facebook+instagram
print("total cost: " + str(sum) + " $")
print("cost in NIS: " + str((sum)*3.5) + " NIS" )
print("cost in NIS + tax: " + str((sum) * 1.17*3.5)+ " NIS + Tax")

if(sum <= budget):
    print("Successfull " + str(budget-sum) + " $")
else:
    print("unsuccessfull, you need to add " + str(sum-budget) + " $, to the budget")
