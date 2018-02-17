"""
Methods for encoding Chip's Challenge (CC) data from JSON files to binary DAT files
Created for the class Programming for Game Designers
"""

import cc_data
import json

''' make a CCDataFile object from a JSON file '''
def make_cc_data_file_from_json(json_data):
    cc_file = cc_data.CCDataFile()

    #for each level in the json file,
    for level_data in json_data:
        # interpret the level
        lvl = make_level(level_data)
        # append it to the levels of our data file
        cc_file.levels.append(lvl)
    # return the game
    return cc_file


''' make a level from the json data '''
def make_level(level_data):
    # gather level data
    cc_level = cc_data.CCLevel()
    cc_level.level_number = level_data["level_num"]
    cc_level.num_chips = level_data["chips_num"]
    cc_level.time = level_data["time"]
    cc_level.upper_layer = level_data["upper_layer"]
    cc_level.lower_layer = level_data["lower_layer"]
    # add optional fields
    opt_fields = add_opt_fields(level_data["opt_fields"])
    cc_level.optional_fields = opt_fields
    return cc_level


def add_opt_fields(opt_fields):
    optional_field_list = []
    for field in opt_fields:
        t = field["type"]
        name = field["Name"]
        val = field["value"]

        if (name == "title") and (t == 3):
            field_dat = cc_data.CCMapTitleField(val)
        elif (name == "brown buttons") and (t == 4):
            add_traps(val)
        elif (name == "red buttons") and (t == 5):
            add_machines(val)
        elif (name == "password") and (t == 6):
            field_dat = cc_data.CCEncodedPasswordField(val)
        elif (name == "hint") and (t == 7):
            field_dat = cc_data.CCMapHintField(val)
        elif (name == "monsters") and (t == 10):
            add_monsters(val)
        optional_field_list.append(field_dat)
    return optional_field_list

def add_traps(val):
    # list of trap coors
        coors = []
        for coor in val:
            # button x and y
            bx = coor['bx']
            by = coor['by']
            # trap x and y
            tx = coor['tx']
            ty = coor['ty']
            coors.append(cc_data.CCTrapControl(bx, by, tx, ty))
        field_dat = cc_data.CCTrapControlsField(coors)

def add_machines(val):
    # list of machine coors
        coors = []
        for coor in val:
            # button x and y
            bx = coor['bx']
            by = coor['by']
            # machine x and y
            mx = coor['mx']
            my = coor['my']
            coors.append(cc_data.CCCloningMachineControl(bx, by, mx, my))
        field_dat = cc_data.CCCloningMachineControlsField

def add_monsters(val):
    # list of monster coors
        coors = []
        for coor in val:
            # monster x and y
            x = coor['x']
            y = coor['y']
            coors.append(cc_data.CCCoordinate(x, y))
        field_dat = cc_data.CCMonsterMovementField(coors)