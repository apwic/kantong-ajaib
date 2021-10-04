from load import *

def borrow_gadget(gadget_log, borrow_gadget_log, id_user):

    id_gadget = input("Masukkan ID Item: ")
    tersedia = False
    returned = False

    for i in range(len(gadget_log)):
        if gadget_log[i]["id"] == id_gadget:
            tersedia = True
        
    for i in range(len(borrow_gadget_log)):
        if borrow_gadget_log[i]["id_gadget"] == id_gadget:
        
            if borrow_gadget_log[i]["id_peminjam"] == id_user and borrow_gadget_log[i]["is_returned"] == "True":
                returned = True
                break

            else:
                returned = False
                break

        else:
            returned = True


    # for i in range(len(borrow_gadget_log)):
    #     if borrow_gadget_log[i]["id_peminjam"] == id_user:
    #         returned = False

    if tersedia:

        if returned:
            tanggal_pinjam = input("Tanggal peminjaman: ")
            jumlah_pinjam = input("Jumlah peminjaman: ")
            length_borrow_gadget = len(borrow_gadget_log)

            for i in range(len(gadget_log)):
                if gadget_log[i]["id"] == id_gadget:

                    if int(gadget_log[i]["jumlah"]) >= int(jumlah_pinjam):
                        print("Item {} (x{}) berhasil dipinjam!".format(gadget_log[i]["nama"], jumlah_pinjam))
                        borrow_gadget_log.append({"id": [], "id_peminjam": [], "id_gadget" : [], "tanggal_peminjaman" : [], "jumlah" : [], "is_returned": False})
                        borrow_gadget_log[length_borrow_gadget]["id"] = length_borrow_gadget
                        borrow_gadget_log[length_borrow_gadget]["id_peminjam"] = id_user
                        borrow_gadget_log[length_borrow_gadget]["id_gadget"] = id_gadget
                        borrow_gadget_log[length_borrow_gadget]["tanggal_peminjaman"] = tanggal_pinjam
                        borrow_gadget_log[length_borrow_gadget]["jumlah"] = jumlah_pinjam
                        break

                    else:
                        print("Jumlah peminjaman melebihi kapasitas yang tersedia. Peminjaman gagal.")
        
        else:
            print("Gadget sudah pernah dipinjam dan belum dikembalikan")

    else:
        print("ID Gadget tidak valid.")


                



