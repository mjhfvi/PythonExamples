"""
(local definition) userMenu
This definition is for the user menu
"""
################## Libraries ##################
import os
import time
# import argparse
from termcolor import colored, cprint
from progress.bar import Bar

################## Files ######################
from apiRequests import *
from writeFile import *

################## End ########################
menu_wait_time = 2 # time.sleep(menu_wait_time)

try:
  def userMenu():
    while (True):
      os.system('clear')
      choice = input("\nSelect from the List: \n\n"
                      "1. Select Product\n"
                      "2. Enter Product Manually \n"
                      "3. Test Connection \n"
                      "4. Download Application \n"
                      "5. Write Version to File? \n"
                      "e. Exit\n\n")
      if choice == "1": # Menu - Select Product
        os.system('clear')
        choice = input("\nSelect from the List: \n\n"
                      "1. ElasticSearch \n"
                      "2. HashiCorp Vault \n"
                      "3. HashiCorp Consul \n"
                      "4. TBD \n"
                      "b. Back\n\n")
        if choice == "1": # ElasticSearch
          userMenu_send_to_apiRequest('elasticsearch', 'https://api.github.com/repos/elastic/elasticsearch/releases/latest')
          # time.sleep(menu_wait_time)
          continue
        elif choice == "2": # HashiCorp Vault
          userMenu_send_to_apiRequest('vault', 'https://api.github.com/repos/hashicorp/vault/releases/latest')
          continue
        elif choice == "3": # HashiCorp Consul
          userMenu_send_to_apiRequest('consul', 'https://api.github.com/repos/hashicorp/consul/releases/latest')
          continue
        elif choice.lower() == "b": # Back
          continue
        continue
      elif choice == "2": # Menu - Enter Product Manually
        custom_product = input('\ninput the url: ')
        userMenu_send_to_apiRequest('user input', custom_product)
        continue
      elif choice == "3": # Menu - Test Connection
        os.system('clear')
        continue
      elif choice == "4": # Menu - Download Application
        os.system('clear')
        continue
      elif choice == "5": # Menu - Write Version to File?
        get_value_from_apiRequest_result = get_value_from_apiRequest('elasticsearch', 'https://api.github.com/repos/elastic/elasticsearch/releases/latest')
        # print(get_value_from_apiRequest_result)
        time.sleep(menu_wait_time)
        # input("\n\nPress Enter to Continue...")
        userMenu_send_to_writeToFile(get_value_from_apiRequest_result)
        os.system('clear')
        continue
      elif choice.lower() == "e": # Exit
        os.system('clear')
        cprint('Exiting Menu...', 'green', 'on_blue')
      break
    # else:
    #   raise Exception('error x02 in menu')
  # except ValueError as error:
  #   print(error)
  #   continue
  #   time.sleep(menu_wait_time)

except KeyboardInterrupt:
  print("User Send Keyboard Interrupt")
finally:
  print("Something else went wrong")

def userMenu_send_to_apiRequest(product_name, api_url):
  os.system('clear')
  print('Getting API Information for ' + product_name,)
  progress_bar()
  print('The latest version of ' + product_name, 'is:', api_request(api_url))
  input("\n\nPress Enter to Continue...")
  cprint('Returning to Menu', 'blue')
  time.sleep(menu_wait_time)
  os.system('clear')

def main_send_to_apiRequest(product_name, api_url):
  os.system('clear')
  print('Getting API Information for ' + product_name,)
  progress_bar()
  print('The latest version of ' + product_name, 'is:', api_request(api_url))
  input("\n\nPress Enter to Continue...")
  cprint('Exiting ...', 'green', 'on_blue')
  time.sleep(menu_wait_time)
  os.system('clear')

def userMenu_send_to_writeToFile(menu_api_data):
  os.system('clear')
  print('Writing ' + menu_api_data, 'to File')
  progress_bar()
  # time.sleep(menu_wait_time)
  writeToFile(menu_api_data)
  print('Done.. Data Saved in File')

def get_value_from_apiRequest(product_name, api_url):
  os.system('clear')
  print(api_request(api_url))
  api_data = api_request(api_url)
  input("\n\nPress Enter to Continue...")
  return api_data

def progress_bar():
  bar = Bar('Processing', max=100)
  for i in range(100):
      time.sleep(0.01)
      bar.next()
  bar.finish()