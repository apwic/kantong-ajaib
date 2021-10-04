import argparse
import os
from parse import *


def load():
    parser = argparse.ArgumentParser()
    parser.add_argument("nama_folder", help="Folder untuk load data csv", type=str)
    args = parser.parse_args()
    file_path = os.getcwd() + "/" + args.nama_folder + "/"

    print("Loading...")
    print("\n")

    return(file_path)

# Fungsi untuk load user.csv menjadi sebuah list of dictionary dan akan dipakai untuk menjadi struktur data internal
def load_user(file):

    user = []

    with open(file + "user.csv", "r") as reader:
        for lines in reader:
            temp_arr = parse(lines, ";")
            temp_dict = {}
            temp_dict["id"] = temp_arr[0]
            temp_dict["username"] = temp_arr[1]
            temp_dict["nama"] = temp_arr[2]
            temp_dict["password"] = temp_arr[3]
            temp_dict["alamat"] = temp_arr[4]
            temp_dict["role"] = temp_arr[5].replace("\n", "")
            user.append(temp_dict)

    return user


# Fungsi untuk load gadget.csv menjadi sebuah list of dictionary dan akan dipakai untuk menjadi struktur data internal
def load_gadget(file):

    gadget = []

    with open(file + "gadget.csv", "r") as reader:
        for lines in reader:
            temp_arr = parse(lines, ";")
            temp_dict = {}
            temp_dict["id"] = temp_arr[0]
            temp_dict["nama"] = temp_arr[1]
            temp_dict["deskripsi"] = temp_arr[2]
            temp_dict["jumlah"] = temp_arr[3]
            temp_dict["rarity"] = temp_arr[4]
            temp_dict["tahun_ditemukan"] = temp_arr[5].replace('\n', "")
            gadget.append(temp_dict)

    return gadget


# Fungsi untuk load consumable.csv menjadi sebuah list of dictionary dan akan dipakai untuk menjadi struktur data internal
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


# Fungsi untuk load gadget_borrow_history.csv menjadi sebuah list of dictionary dan akan dipakai untuk menjadi struktur data internal
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


# Fungsi untuk load consumable_history.csv menjadi sebuah list of dictionary dan akan dipakai untuk menjadi struktur data internal
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


# Fungsi untuk load gadget_return_history.csv menjadi sebuah list of dictionary dan akan dipakai untuk menjadi struktur data internal
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