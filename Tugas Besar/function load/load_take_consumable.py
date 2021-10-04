from parse import *

def load_take_consumable(file):

    take_consumable = []

    with open(file + "consumable_history.csv", "r") as reader:
        for lines in reader:
            temp_arr = parse(lines, ";")
            temp_dict = {}
            temp_dict["id"] = temp_arr[0]
            temp_dict["id_pengambil"] = temp_arr[1]
            temp_dict["id_consumable"] = temp_arr[2]
            temp_dict["tanggal_pengambilan"] = temp_arr[3]
            temp_dict["jumlah"] = temp_arr[4].replace('\n', "")
            take_consumable.append(temp_dict)

    return take_consumable