from load import *

def take_consumable(consumable_log, take_consumable_log, id_user):

    id_consumable = input("Masukkan ID Item: ")
    tersedia = False

    for i in range(len(consumable_log)):
        if consumable_log[i]["id"] == id_consumable:
            tersedia = True

    if tersedia:

        tanggal_minta = input("Tanggal pengambilan: ")
        jumlah_minta = input("Jumlah pengambilan: ")
        length_take_consumable = len(take_consumable_log)

        for i in range(len(consumable_log)):

            if consumable_log[i]["id"] == id_consumable:
                if int(consumable_log[i]["jumlah"]) >= int(jumlah_minta):
                    take_consumable_log.append({"id": [], "id_pengambil": [], "id_consumable" : [], "tanggal_pengambilan" : [], "jumlah" : []})
                    take_consumable_log[length_take_consumable]["id"] = length_take_consumable
                    take_consumable_log[length_take_consumable]["id_pengambil"] = id_user
                    take_consumable_log[length_take_consumable]["id_consumable"] = id_consumable
                    take_consumable_log[length_take_consumable]["tanggal_pengambilan"] = tanggal_minta
                    take_consumable_log[length_take_consumable]["jumlah"] = jumlah_minta
                    print("Item {} (x {}) telah berhasil diambil!".format(consumable_log[i]["id"], jumlah_minta))

                else:
                    print("Jumlah pengambilan melebihi kapasitas yang tersedia. Peminjaman gagal.")

    else:
        print("ID Consumable tidak valid.")


