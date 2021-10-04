from load import *

def return_gadget(gadget, borrow_gadget_log, return_gadget_log, id_user):

    nama = []
    id_gadget = []
    n_gadget = []
    id_peminjaman = []
    jumlah_dipinjam = []
    valid = False

    for i in range(1, len(borrow_gadget_log)):
        for j in range(1, len(gadget)):
            if (borrow_gadget_log[i]["id_gadget"] == gadget[j]["id"]) and (borrow_gadget_log[i]["is_returned"] == "False") and (borrow_gadget_log[i]["id_peminjam"] == id_user):
                # nama.append(gadget[i]["nama"])
                id_peminjaman.append(borrow_gadget_log[i]["id"])
                id_gadget.append(borrow_gadget_log[i]["id_gadget"])
                jumlah_dipinjam.append(borrow_gadget_log[i]["jumlah"])
                n_gadget.append(j)
                valid = True

    for i in range(1, len(gadget)):
        for j in range(len(id_gadget)):
            if id_gadget[j] == gadget[i]["id"]:
                nama.append(gadget[i]["nama"])

    # print(id_gadget)
    # print(nama)
    if valid:

        for i in range(len(nama)):
            print(f"{i+1}. {nama[i]} (x {jumlah_dipinjam[i]})")

        n = int(input("Masukan nomor peminjaman: ")) - 1
        tanggal = input("Tanggal pengembalian: ")
        jumlah_pengembalian = int(input("Jumlah pengembalian: "))
        jumlah_awal = int(gadget[int(n_gadget[n])]["jumlah"])
        jumlah_peminjaman = int(borrow_gadget_log[int(id_peminjaman[n])]["jumlah"])

        if 1 <= jumlah_pengembalian < jumlah_peminjaman:
            gadget[int(n_gadget[n])]["jumlah"] = str(jumlah_awal + jumlah_pengembalian)
            return_gadget_log.append({})
            return_gadget_log[len(return_gadget_log)-1]["id"] = len(return_gadget_log) - 1
            return_gadget_log[len(return_gadget_log)-1]["id_peminjaman"] = id_peminjaman[n]
            return_gadget_log[len(return_gadget_log)-1]["tanggal_pengembalian"] = tanggal
            return_gadget_log[len(return_gadget_log)-1]["jumlah_pengembalian"] = str(jumlah_pengembalian)
            print(f"Item {nama[n]} (x {jumlah_pengembalian}) telah dikembalikan")

        elif jumlah_pengembalian == jumlah_peminjaman:
            gadget[int(n_gadget[n])]["jumlah"] = str(jumlah_awal + jumlah_pengembalian)
            borrow_gadget_log[int(id_peminjaman[n])]["is_returned"] = True
            return_gadget_log.append({})
            return_gadget_log[len(return_gadget_log)-1]["id"] = len(return_gadget_log)-1
            return_gadget_log[len(return_gadget_log)-1]["id_peminjaman"] = id_peminjaman[n]
            return_gadget_log[len(return_gadget_log)-1]["tanggal_pengembalian"] = tanggal
            return_gadget_log[len(return_gadget_log)-1]["jumlah_pengembalian"] = str(jumlah_pengembalian)
            print(f"Item {nama[n]} (x {jumlah_pengembalian}) telah dikembalikan")

        else:
            print("Jumlah tidak valid")

    else:
        print("Tidak ada history peminjaman.")



    

    

    

    