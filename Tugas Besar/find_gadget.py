from load import *

def gadget_by_rarity(file):

    gadget = load_gadget(file)
    rarity = input("Masukkan rarity: ")
    ada = False

    print("Hasil pencarian:")
    for i in range(1, len(gadget)):
        if rarity == gadget[i]["rarity"]:
            print("\nNama             :", gadget[i]["nama"])
            print("Deskripsi        :", gadget[i]["deskripsi"])
            print("Jumlah           :", gadget[i]["jumlah"])
            print("Rarity           :", gadget[i]["rarity"])
            print("Tahun ditemukan  :", gadget[i]["tahun_ditemukan"])
            ada = True

    if not ada:
        print("Tidak ditemukan gadget dengan rarity", rarity)


def cetak(gadget, index):
    print("\nNama             :", gadget[index]["nama"])
    print("Deskripsi        :", gadget[index]["deskripsi"])
    print("Jumlah           :", gadget[index]["jumlah"])
    print("Rarity           :", gadget[index]["rarity"])
    print("Tahun ditemukan  :", gadget[index]["tahun_ditemukan"])


def gadget_by_year(file):

    gadget = load_gadget(file)
    year = input("Masukkan tahun: ")
    kategori = input("Masukkan kategori: ")
    ada = False

    print("\nHasil pencarian:")
    for i in range(1, len(gadget)):
        if kategori == '='and (year == gadget[i]["tahun_ditemukan"]):
            cetak(gadget, i)
            ada = True
        elif kategori == '>' and (gadget[i]["tahun_ditemukan"] > year):
            cetak(gadget, i)
            ada = True
        elif kategori == '>=' and (gadget[i]["tahun_ditemukan"] >= year):
            cetak(gadget, i)
            ada = True
        elif kategori == '<' and (gadget[i]["tahun_ditemukan"] < year):
            cetak(gadget, i)
            ada = True
        elif kategori == '<=' and (gadget[i]["tahun_ditemukan"] <= year):
            cetak(gadget, i)
            ada = True

    if not ada:
        print("Tidak ada gadget yang ditemukan")
