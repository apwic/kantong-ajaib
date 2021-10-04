import os

def write_register(file, register_log):

    with open(file + "user.csv", "w") as writer:
        
        for i in range(len(register_log)):
            
            idx = register_log[i]["id"]
            username = register_log[i]["username"]
            nama = register_log[i]["nama"]
            password = register_log[i]["password"]
            alamat = register_log[i]["alamat"]
            role = register_log[i]["role"]

            write_value = str(idx) + ';' + username + ';' + nama.title() + ';' + password + ';' + alamat + ';' + role
            writer.write(write_value + "\n")


def write_gadget(file, gadget_log):

    with open(file + "gadget.csv", "w") as writer:

        for i in range(len(gadget_log)):

            idx = gadget_log[i]["id"]
            nama = gadget_log[i]["nama"]
            deskripsi = gadget_log[i]["deskripsi"]
            jumlah = gadget_log[i]["jumlah"]
            rarity = gadget_log[i]["rarity"]
            tahun_ditemukan = gadget_log[i]["tahun_ditemukan"]

            write_value = str(idx) + ";" + nama + ';' + deskripsi + ';' + jumlah + ';' + rarity + ';' + tahun_ditemukan
            writer.write(write_value + "\n")

def write_consumable(file, consumable_log):

    with open(file + "consumable.csv", "w") as writer:

        for i in range(len(consumable_log)):

            idx = consumable_log[i]["id"]
            nama = consumable_log[i]["nama"]
            deskripsi = consumable_log[i]["deskripsi"]
            jumlah = consumable_log[i]["jumlah"]
            rarity = consumable_log[i]["rarity"]

            write_value = str(idx) + ";" + nama + ';' + deskripsi + ';' + jumlah + ';' + rarity
            writer.write(write_value + "\n")


def write_borrow_gadget(file, borrow_gadget_log, gadget, idx_borrow_gadget):

    with open(file + "gadget_borrow_history.csv", "w") as writer:

        for i in range(len(borrow_gadget_log)):

            idx = borrow_gadget_log[i]["id"]
            idx_peminjam = borrow_gadget_log[i]["id_peminjam"]
            idx_gadget = borrow_gadget_log[i]["id_gadget"]
            tanggal_peminjaman = borrow_gadget_log[i]["tanggal_peminjaman"]
            jumlah = borrow_gadget_log[i]["jumlah"]
            is_returned = borrow_gadget_log[i]["is_returned"]

            write_value = str(idx) + ";" + idx_peminjam + ';' + idx_gadget + ';' + tanggal_peminjaman + ';' + jumlah + ';' + str(is_returned)
            writer.write(write_value + "\n")

    for i in range(len(gadget)):
        for j in range(idx_borrow_gadget, len(borrow_gadget_log)):

            if gadget[i]["id"] == borrow_gadget_log[j]["id_gadget"]:
                new_jumlah = int(gadget[i]["jumlah"]) - int(borrow_gadget_log[j]["jumlah"])
                gadget[i]["jumlah"] = str(new_jumlah)


def write_return_gadget(file, return_gadget_log):

    with open(file + "gadget_return_history.csv", "w") as writer:
        
        for i in range(len(return_gadget_log)):
            
            idx = return_gadget_log[i]["id"]
            id_pinjam = return_gadget_log[i]["id_peminjaman"]
            tanggal_pengembalian = return_gadget_log[i]["tanggal_pengembalian"]
            jumlah_kembali = return_gadget_log[i]["jumlah_pengembalian"]

            write_value = str(idx) + ';' + id_pinjam + ';' + tanggal_pengembalian + ';' + jumlah_kembali
            writer.write(write_value + "\n")


def write_consumable_history(file, take_consumable_log, consumable, idx_take_consumable):

    with open(file + "consumable_history.csv", "w") as writer:

        for i in range(len(take_consumable_log)):

            idx = take_consumable_log[i]["id"]
            idx_pengambil = take_consumable_log[i]["id_pengambil"]
            idx_consumable = take_consumable_log[i]["id_consumable"]
            tanggal_pengambilan = take_consumable_log[i]["tanggal_pengambilan"]
            jumlah = take_consumable_log[i]["jumlah"]

            write_value = str(idx) + ";" + idx_pengambil + ';' + idx_consumable + ';' + tanggal_pengambilan + ';' + jumlah
            writer.write(write_value + "\n")

    for i in range(len(consumable)):
        for j in range(idx_take_consumable, len(take_consumable_log)):

            if consumable[i]["id"] == take_consumable_log[j]["id_consumable"]:
                new_jumlah = int(consumable[i]["jumlah"]) - int(take_consumable_log[j]["jumlah"])
                consumable[i]["jumlah"] = str(new_jumlah)
                

def save(register_log, gadget_log, consumable_log, borrow_gadget_log, take_consumable_log, idx_borrow_gadget, idx_take_consumable, return_gadget_log):

    folder = input("Masukkan nama folder penyimpanan: ")
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, folder)

    if not os.path.exists(folder):
        os.mkdir(path)

    write_register(folder + "/", register_log)
    write_consumable_history(folder + "/", take_consumable_log, consumable_log, idx_take_consumable)
    write_return_gadget(folder + "/", return_gadget_log)
    write_borrow_gadget(folder + "/", borrow_gadget_log, gadget_log, idx_borrow_gadget)
    write_gadget(folder + "/", gadget_log)
    write_consumable(folder + "/", consumable_log)

    print("File berhasil di save pada folder {}".format(folder))
    





