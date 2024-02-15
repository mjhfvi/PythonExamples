'''
1.Create a code that will ask for your marketing budget .
    Facebook Campaign = 100$ per day
    Instagram Campaign = 50$ per day

  Ask him:
how long he want the facebook Campaign will run
how long he want the Instagram Campaign will run

And then print to the screen the summary of the cost in ILS with tax ( 17%)
If it is more than his marketing budget , tell him how much to add, if not tell him "successfull"

'''

### Information ###

facebookCampaign = int()
instagramCampaign = int()

facebookCampaign = int(input("please input the number of days you want this facebook Campaign to run: \n"))
instagramCampaign = int(input("please input the number of days you want this Instagram Campaign to run: \n"))

totalPricefacebookCampaign = float(facebookCampaign * 100 * 3.5 * 1.17)
totalPriceinstagramCampaign = float(instagramCampaign * 50 * 3.5 * 1.17)

print(facebookCampaign)
print(totalPricefacebookCampaign)
print("your total prince for Facebook Campaign is: " + str(totalPricefacebookCampaign))
print("your total prince for Instagram Campaign is: " + str(totalPriceinstagramCampaign))