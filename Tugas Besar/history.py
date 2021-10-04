import datetime

def urutkan_riwayat(list_file, tanggal):
    l = len(list_file)
    for i in range(0, l):
        for j in range(1, l-i-1):
            tanggal1 = list_file[j][tanggal]
            tanggal2 = list_file[j+1][tanggal]
            if datetime.date(int(tanggal1[6:]),int(tanggal1[3:5]),int(tanggal1[0:2])) < datetime.date(int(tanggal2[6:]),int(tanggal2[3:5]),int(tanggal2[0:2])):
                tempo = list_file[j]
                list_file[j]= list_file[j + 1]
                list_file[j + 1]= tempo
    return list_file

def tampilkan_gbh(user_log, gadget_log, gadget_borrow_history_log):
    # gbh = load_borrow_gadget()
    # gadget = load_gadgets()
    # user = load_user()
    riwayat_sorted = urutkan_riwayat(gadget_borrow_history_log, "tanggal_peminjaman")
    start = 1
    maxIndex = start
    # print(riwayat_sorted)
    # print(len(riwayat_sorted))
 
    while True:
        if len(riwayat_sorted) - start + 1 > 5:
            maxIndex += 5
        else:
            maxIndex = len(riwayat_sorted)
 
        for i in range(start,maxIndex):
            namaUser = user_log[int(riwayat_sorted[i]["id_peminjam"])]["nama"]
            id_gadget = riwayat_sorted[i]["id_gadget"]
            for j in range(1,len(gadget_log)):
                if id_gadget == gadget_log[j]["id"]:
                    namaGadget = gadget_log[j]["nama"]
                    break
 
            print("\nID peminjaman        :", riwayat_sorted[i]["id"])
            print("Nama peminjam        :", namaUser)
            print("Nama gadget          :", namaGadget)
            print("Tanggal peminjaman   :", riwayat_sorted[i]["tanggal_peminjaman"])
            print("Jumlah               :", riwayat_sorted[i]["jumlah"])
            print("Sudah dikembalikan?  :", riwayat_sorted[i]["is_returned"])
        
        if maxIndex == len(riwayat_sorted):
            break
        else:
            print("\nTelusuri riwayat terdahulu? (Y/N) ")
            konfirmasi = input()
            while konfirmasi.lower() != 'n' and konfirmasi.lower() != 'y':
                konfirmasi = input()
            if konfirmasi.lower() == 'n':
                break
            else:
                start += 5


def tampilkan_return_history(user_log, gadget_log, gadget_borrow_history_log, gadget_return_history_log):

    riwayat_sorted = urutkan_riwayat(gadget_return_history_log, "tanggal_pengembalian")
    start = 1
    maxIndex = start
 
    while True:
        if (len(riwayat_sorted) - start + 1) > 5:
            maxIndex += 5
        else:
            maxIndex = len(riwayat_sorted)
 
        for i in range(start,maxIndex):
            namaUser = user_log[int(riwayat_sorted[i]["id_peminjaman"])]["nama"]
            id_gadget = gadget_borrow_history_log[int(riwayat_sorted[i]["id"])]["id_gadget"]
            for j in range(1,len(gadget_log)):
                if id_gadget == gadget_log[j]["id"]:
                    namaGadget = gadget_log[j]["nama"]
                    break
 
            print("\nID Pengembalian      :", riwayat_sorted[i]["id"])
            print("Nama Peminjam        :", namaUser)
            print("Nama Gadget          :", namaGadget)
            print("Tanggal Pengembalian :", riwayat_sorted[i]["tanggal_pengembalian"])
            print("Jumlah Pengembalian  :", riwayat_sorted[i]["jumlah_pengembalian"])
        
        if maxIndex == len(riwayat_sorted):
            break
        
        else:
            print("\nTelusuri riwayat terdahulu? (y/n) ")
            konfirmasi = input()
            while konfirmasi != 'n' and konfirmasi != 'y':
                konfirmasi = input()
            if konfirmasi == 'n':
                break
            else:
                start += 5


def tampilkan_take_consumable(user_log, consumable_log, take_consumable_log):

    take_consumable_sorted = urutkan_riwayat(take_consumable_log, "tanggal_pengambilan")
    start = 1
    maxIndex = start
 
    while True:
        if len(take_consumable_sorted) - start + 1 > 5:
            maxIndex += 5
        else:
            maxIndex = len(take_consumable_sorted)
 
        for i in range(start,maxIndex):
            namaUser = user_log[int(take_consumable_sorted[i]["id_pengambil"])]["nama"]
            id_consumable = take_consumable_sorted[i]["id_consumable"]
            for j in range(1,len(consumable_log)):
                if id_consumable == consumable_log[j]["id"]:
                    nama_consumable = consumable_log[j]["nama"]
                    break
 
            print("\nID Pengambilan       :", take_consumable_sorted[i]["id"])
            print("Nama peminjam        :", namaUser)
            print("Nama consumable      :", nama_consumable)
            print("Tanggal Pengambilan  :", take_consumable_sorted[i]["tanggal_pengambilan"])
            print("Jumlah               :", take_consumable_sorted[i]["jumlah"])
        
        if maxIndex == len(take_consumable_sorted):
            break
        else:
            print("\nTelusuri riwayat terdahulu? (y/n) ")
            konfirmasi = input()
            while konfirmasi != 'n' and konfirmasi != 'y':
                konfirmasi = input()
            if konfirmasi == 'n':
                break
            else:
                start += 5


