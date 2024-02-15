"""
this is a demo project
1. build api to get information
2. user input for custom urls
3. built-in url
4. menu to select product
5. use multiple files for every class
6. add help menu for the user
7. read and write to files for cache
8. add UI for user
9. add progress bar for downloads
"""
################## Libraries ##################
from termcolor import colored, cprint
import argparse

################## Files ######################
from userMenu import *
from commandLineArguments import *
from apiRequests import *

################## End ########################

def main():
  if commandLineArguments():
    main_send_to_apiRequest('testing02', commandLineArguments())
  else:
    userMenu()

if __name__ == "__main__":
  try:
    main()
    # time.sleep(3)
    # raise Exception('error x01 on main')
  except KeyboardInterrupt:
    os.system('clear')
    cprint('User Send Keyboard Interrupt', 'green', 'on_red', attrs=['bold'])
