"""
(local definition) apiRequests
this definition is for sending api requests and receive the version from the tag
"""
################## Libraries ##################
import requests

################## Files ######################

################## End ########################

def api_request(product_url_api):
  try:
    response = requests.get(product_url_api)
    if response.status_code == 200:
      api_information = response.json()
      latest_version = api_information['tag_name']
      # api_url = api_information['html_url']
      # print('API Endpoint :', api_url)
      return latest_version
    else:
      print(f"Failed to retrieve latest Elasticsearch version. Status code: {response.status_code}")
      return None
  except Exception as e:
    print(f"An error occurred: {e}")
    return None

# latest_version = api_request()
# if latest_version:
#   print(f"The latest version of Elasticsearch is: {latest_version}")
# else:
#   print("Failed to retrieve the latest version.")

# def get_version_from_api():
#   try:
#     print('api information is:', latest_version)
#     latest_version = api_request()
#     if latest_version:
#       print(f"The latest version of Elasticsearch is: {latest_version}")
#       return latest_version
#     else:
#       print("Failed to retrieve the latest version.")
#   except Exception as e:
#     print(f"An error occurred: {e}")
#     return None

# print(api_request())