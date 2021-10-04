from parse import *

def load_borrow_gadget(file):

    borrow_gadget = []

    with open(file + "gadget_borrow_history.csv", "r") as reader:
        for lines in reader:
            temp_arr = parse(lines, ";")
            temp_dict = {}
            temp_dict["id"] = temp_arr[0]
            temp_dict["id_peminjam"] = temp_arr[1]
            temp_dict["id_gadget"] = temp_arr[2]
            temp_dict["tanggal_peminjaman"] = temp_arr[3]
            temp_dict["jumlah"] = temp_arr[4]
            temp_dict["is_returned"] = temp_arr[5].replace('\n', "")
            borrow_gadget.append(temp_dict)

    return borrow_gadget