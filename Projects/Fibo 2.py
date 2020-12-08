fibo=[1,2,3,5,8,13,21]
#0 1 2 3 4 5 6
boolean="True"
#for i in range (2,7):

for i range(2, len(fibo)):
    print(fibo[i])
    print(fibo[i-1])
    print(fibo[i-2])
    if fibo[i]==(fibo[i-1]+fibo[i-2]):
        continue
    else:
        boolean="False"
        break
if boolean=="True"
    print("it is fibo series")
else:
    print("it isn't fibo series")


