from parse import *

def load_consumable(file):

    consumable = []

    with open(file + "consumable.csv", "r") as reader:
        for lines in reader:
            temp_arr = parse(lines, ";")
            temp_dict = {}
            temp_dict["id"] = temp_arr[0]
            temp_dict["nama"] = temp_arr[1]
            temp_dict["deskripsi"] = temp_arr[2]
            temp_dict["jumlah"] = temp_arr[3]
            temp_dict["rarity"] = temp_arr[4].replace('\n', "")
            consumable.append(temp_dict)

    return consumable