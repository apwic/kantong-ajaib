from load import *

def change_item(gadget_log, consumable_loggadget_log):

    gaib = True
    id_item = input("Masukkan ID: ")
 
    if id_item[0] == 'G':
        # gadget_log = load_gadget_log()
        for i in range(1,len(gadget_log)):
            if id_item == gadget_log[i]["id"]:
 
                jumlah = input("Masukkan jumlah: ")
                jumlahAkhir = int(jumlah) + int(gadget_log[i]["jumlah"])
 
                if jumlah[0] == '-':
                    if jumlahAkhir < 0:
                        print("{} {} berhasil dibuang. Stok sekarang: {}".format(jumlah[1:], gadget_log[i]["nama"], jumlahAkhir))
                    else:
                        gadget_log[i]["jumlah"] = str(jumlahAkhir)
                        # gad = open("gadget_log.csv", "r")
                        # list_of_lines = gad.readlines()
 
                        # nama = gadget_log[i]["nama"]
                        # deskripsi = gadget_log[i]["deskripsi"]
                        # rarity = gadget_log[i]["rarity"]
                        # tahun = gadget_log[i]["tahun_ditemukan"]
 
                        # write_line = id_item + ';' + nama + ';' + deskripsi + ';' + str(jumlahAkhir) + ';' + rarity + ';' + tahun + "\n"
                        # list_of_lines[i] = write_line
 
                        # gad = open("gadget_log.csv", "w")
                        # gad.writelines(list_of_lines)
                        # gad.close()
 
                        print("{} {} berhasil dibuang. Stok sekarang: {}".format(jumlah[1:], gadget_log[i]["nama"], jumlahAkhir))
                else:
                    gadget_log[i]["jumlah"] = str(jumlahAkhir)
                    # gad = open("gadget_log.csv", "r")
                    # list_of_lines = gad.readlines()
 
                    # nama = gadget_log[i]["nama"]
                    # deskripsi = gadget_log[i]["deskripsi"]
                    # rarity = gadget_log[i]["rarity"]
                    # tahun = gadget_log[i]["tahun_ditemukan"]
 
                    # write_line = id_item + ';' + nama + ';' + deskripsi + ';' + str(jumlahAkhir) + ';' + rarity + ';' + tahun + "\n"
                    # list_of_lines[i] = write_line
 
                    # gad = open("gadget_log.csv", "w")
                    # gad.writelines(list_of_lines)
                    # gad.close()
 
                    print("{} {} berhasil ditambahkan. Stok sekarang: {}".format(jumlah, gadget_log[i]["nama"], jumlahAkhir))
                gaib = False
                break
        
        if gaib:
            print("ID gadget tidak tersedia")
 
    elif id_item[0] == 'C':
        # consumable_log = load_consumable_logs()
        for i in range(1,len(consumable_log)):
            if id_item == consumable_log[i]["id"]:
 
                jumlah = input("Masukkan jumlah: ")
                jumlahAkhir = int(jumlah) + int(consumable_log[i]["jumlah"])
 
                if jumlah[0] == '-':
                    if jumlahAkhir < 0:
                        print("{} {} berhasil dibuang. Stok sekarang: {}".format(jumlah[1:], consumable_log[i]["nama"], jumlahAkhir))

                    else:
                        consumable_log[i]["jumlah"] = str(jumlahAkhir)
                        # cons = open("consumable_log.csv", "r")
                        # list_of_lines = cons.readlines()
 
                        # nama = consumable_log[i]["nama"]
                        # deskripsi = consumable_log[i]["deskripsi"]
                        # rarity = consumable_log[i]["rarity"]
 
                        # write_line = id_item + ';' + nama + ';' + deskripsi + ';' + str(jumlahAkhir) + ';' + rarity + ';' + "\n"
                        # list_of_lines[i] = write_line
 
                        # cons = open("consumable_log.csv", "w")
                        # cons.writelines(list_of_lines)
                        # cons.close()
 
                        print("{} {} berhasil dibuang. Stok sekarang: {}".format(jumlah[1:], consumable_log[i]["nama"], jumlahAkhir))
                        
                else:
                    consumable_log[i]["jumlah"] = str(jumlahAkhir)
                    # cons = open("consumable_log.csv", "r")
                    # list_of_lines = cons.readlines()
 
                    # nama = consumable_log[i]["nama"]
                    # deskripsi = consumable_log[i]["deskripsi"]
                    # rarity = consumable_log[i]["rarity"]
 
                    # write_line = id_item + ';' + nama + ';' + deskripsi + ';' + str(jumlahAkhir) + ';' + rarity + ';' + "\n"
                    # list_of_lines[i] = write_line
 
                    # cons = open("consumable_log.csv", "w")
                    # cons.writelines(list_of_lines)
                    # cons.close()
 
                    print("{} {} berhasil ditambahkan. Stok sekarang: {}".format(jumlah, consumable_log[i]["nama"], jumlahAkhir))
 
                gaib = False
                break
        
        if gaib:
            print("ID consumable tidak tersedia")
 
    else:
        print("ID tidak valid!")