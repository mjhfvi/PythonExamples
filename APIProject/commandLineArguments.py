"""
(local definition) commandLineArguments
This definition is for the user Command-Line Arguments
"""
################## Libraries ##################
# import sys
import argparse
################## Files ######################


################## End ########################

def commandLineArguments():
  parser = argparse.ArgumentParser(description="Command Line Arguments")
  parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
  parser.add_argument('-u', '--url', help="input the url from github")
  # parser.add_argument('-n', '--name', help="input the application name")
  args = parser.parse_args()
  return args.url


#   if args.verbose:
#     print("verbosity turned on")

#   if args.url:
#     print("Custom message:", args.url)

#   if args.name:
#     print("Custom message:", args.name)

# if __name__ == "__main__":
#   commandLineArguments()