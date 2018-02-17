import cc_dat_utils
import test_data
import test_json_utils
import cc_json_utils
import json

#Part 1
#Use cc_data_utils.make_cc_data_from_dat() to load pfgd_test.dat
#print the resulting data
dat = cc_dat_utils.make_cc_data_from_dat("data/pfgd_test.dat")
# print(dat)


#Part 2
#Open the file specified by input_json_file
input_json_file = "data/test_data.json"
#Use the json module to load the data from the file
with open (input_json_file) as reader:
    library_data = json.load(reader)
    
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
#Print out the resulting GameLibrary data using print_game_library(game_library_data) in test_data.py
# library = test_json_utils.make_game_library_from_json(library_data)


#Part 3
#Load your custom JSON file
with open("data/jbfields_cc1.json") as reader:
    json_dat = json.load(reader)

#Convert JSON data to cc_data
data_file = cc_json_utils.make_cc_data_file_from_json(json_dat)
#Save converted data to DAT file
cc_dat_utils.write_cc_data_to_dat(data_file, "data/jbfields_cc1.dat")