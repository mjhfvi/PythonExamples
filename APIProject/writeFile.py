"""
(local definition) writeFile
This definition is for the user Command-Line Arguments
"""
################## Libraries ##################
import json
import io
################## Files ######################

################## End ########################

# Write JSON file
def writeToFile(file_data):
  with io.open('data.json', 'w', encoding='utf8') as outfile:
    file_data = json.dumps(file_data, indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=False)
    outfile.write((file_data))

# Read JSON file
def readFromFile():
  with open('data.json') as data_file:
    data_loaded = json.load(data_file)