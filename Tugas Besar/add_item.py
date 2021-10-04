from load import *

def cek_gadget(gadget, idx):

    tersedia = True

    for i in range(1,len(gadget)):

        if idx == gadget[i]["id"]:
            print("Gagal menambahkan item karena ID sudah ada")
            tersedia = False
            break

    return tersedia


def cek_consumable(consumable,idx):

    tersedia = True
    
    for i in range(1,len(consumable)):
            
            if idx == consumable[i]["id"]:
                print("Gagal menambahkan item karena ID sudah ada")
                tersedia = False
                break

    return tersedia


def tambah_gadget(id_gadget, gadget_log):

    length_gadget = len(gadget_log) 

    gadget_log.append({"id": [], "nama": [], "deskripsi": [], "jumlah": [], "rarity": [], "tahun_ditemukan": []})
    gadget_log[length_gadget]["id"] = id_gadget
    gadget_log[length_gadget]["nama"] = input("Masukan Nama: ")
    gadget_log[length_gadget]["deskripsi"] = input("Masukan Deskripsi: ")
    gadget_log[length_gadget]["jumlah"] = input("Masukan Jumlah: ")
    gadget_log[length_gadget]["rarity"] = input("Masukan Rarity: ")
    gadget_log[length_gadget]["tahun_ditemukan"] = input("Masukkan tahun ditemukan: ")
    print("Item telah berhasil ditambahkan ke database.")


def tambah_consumable(id_consumable, consumable_log):

    length_consumable = len(consumable_log)

    consumable_log.append({"id": [], "nama": [], "deskripsi": [], "jumlah": [], "rarity": []})
    consumable_log[length_consumable]["id"] = id_consumable
    consumable_log[length_consumable]["nama"] = input("Masukan Nama: ")
    consumable_log[length_consumable]["deskripsi"] = input("Masukan Deskripsi: ")
    consumable_log[length_consumable]["jumlah"] = input("Masukan Jumlah: ")
    consumable_log[length_consumable]["rarity"] = input("Masukan Rarity: ")
    print("Item telah berhasil ditambahkan ke database.")




