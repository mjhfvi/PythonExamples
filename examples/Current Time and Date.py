'''
Current Time and Date
'''

from datetime import datetime

now=datetime.now()

date=now.strftime("%H:%M:%S")
time=now.date()
print("Current Time =", date + "\nCurrent Date =", time)