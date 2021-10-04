from load import *

# def cek_delete(gadget, consumable, idx):
    
#     i = 0
#     j = 0
#     found_gadget = False
#     found_consumable = False

#     while (not (found_gadget)) and (i != len(gadget)):

#         if gadget[i]["id"] == idx:
#             found_gadget = True

#         i += 1

#     while (not (found_consumable)) and (j != len(consumable)):

#         if consumable[j]["id"] == idx:
#             found_consumable = True

#         j += 1

#     if found_gadget:
#         return found_gadget
    
#     elif found_consumable:
#         return found_consumable

#     else:
#         return found_gadget or found_consumable
#         print("Tidak ada item dengan ID tersebut.")

# id_hapus = input("Masukkan ID item: ")

# if cek_delete(gadget_log_main, consumable_log_main, id_hapus):
#     for i in range(len(gadget_log_main)):
#         if gadget_log_main[i]["id"] == id_hapus:
#             nama_hapus = gadget_log_main[i]["nama"]

#     for j in range(len(consumable_log_main)):
#         if consumable_log_main[j]["id"] == id_hapus:
#             nama_hapus = consumable_log_main[i]["nama"]

#     validasi_hapus = input(f"Apakah anda yakin ingin menghapus {nama_hapus} (Y/N)?")

# if validasi_hapus:
#     delete_item(gadget_log_main, consumable_log_main, id_hapus)

def delete_item(gadget, consumable):

    id_hapus = input("Masukkan ID item: ")
    i = 0
    j = 0
    validasi_hapus = ""
    found_gadget = False
    found_consumable = False

    while (not (found_gadget)) and (i != len(gadget)):
        if gadget[i]["id"] == id_hapus:
            nama_hapus = gadget[i]["nama"]
            found_gadget = True
        i += 1

    while (not (found_consumable)) and (j != len(consumable)):
        if consumable[j]["id"] == id_hapus:
            nama_hapus = consumable[i]["nama"]
            found_consumable = True
        j += 1

    if found_consumable or found_gadget:
        validasi_hapus = input(f"Apakah anda yakin ingin menghapus {nama_hapus} (Y/N)?")
    else:
        print("Tidak ada item dengan ID tersebut.")
    

    if validasi_hapus.lower() == "y":
        flag_hapus = True
    else:
        flag_hapus = False


    if flag_hapus and found_gadget:
        for i in range(len(gadget)):
            if gadget[i]["id"] == id_hapus:
                gadget.remove(gadget[i])
        print("Item telah berhasil dihapus dari database.")

    elif flag_hapus and found_consumable:
        for i in range(len(consumable)):
            if consumable[j]["id"] == id_hapus:
                consumable.remove(consumable[i])
        print("Item telahl berhasil dihapus dari database.")

