from parse import *

def load_return_gadget(file):

    return_gadget = []

    with open(file + "gadget_return_history.csv", "r") as reader:
        for lines in reader:
            temp_arr = parse(lines, ";")
            temp_dict = {}
            temp_dict["id"] = temp_arr[0]
            temp_dict["id_peminjaman"] = temp_arr[1]
            temp_dict["tanggal_pengembalian"] = temp_arr[2]
            temp_dict["jumlah_pengembalian"] = temp_arr[3].replace('\n', "")
            return_gadget.append(temp_dict)

    return return_gadget

# print(load_return_gadget("data/"))