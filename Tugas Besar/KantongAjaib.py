from register import *
from login import *
from find_gadget import *
from borrow_gadget import *
from take_consumable import *
from add_item import *
from return_gadget import *
from delete_item import *
from change_item import *
from history import *
from save import *
from load import *
from helpp import *


file_path = load()

# Inisialisasi Log
user_log_main = load_user(file_path)
gadget_log_main = load_gadget(file_path)
consumable_log_main = load_consumable(file_path)
borrow_gadget_log_main = load_borrow_gadget(file_path)
return_gadget_log_main = load_return_gadget(file_path)
take_consumable_log_main = load_take_consumable(file_path)

idx_borrow_gadget = len(borrow_gadget_log_main)
idx_take_consumable = len(take_consumable_log_main)

# Welcome message
print("Selamat Datang! Silahkan pilih menu terlebih dahulu")
print("- Login")
print("- help")
print("- Exit")


choice = input("\nSilahkan pilih menu: ")                            # Inisialisasi untuk input menu dari pengguna
flag_login = False
role_user = ""


# Loop login, pengguna diwajibkan untuk login terlebih dahulu
while (not flag_login):                                            

    # Login akan mengulang sampai pengguna memasukkan username dan password yang sesuai
    if choice.lower() == "login":
        validasi = False
        while (not validasi):
            login_main = login(file_path)
            validasi = login_main[0]
            role_user = login_main[1]
            id_user = login_main[2]
        flag_login = True


    elif choice.lower() == "exit":
        print("Terima Kasih sudah menggunakan program kami!")
        flag_login = True

    elif choice.lower() == "help":
            helpadm(file_path)
            choice = input("\nSilahkan pilih menu: ")

    else:
        print("Menu tidak tersedia. Silahkan input menu yang valid.")
        choice = input("\nSilahkan pilih menu: ")


# Loop untuk program utama
# Tergantung role, maka menu yang tersedia akan berbeda
flag_main = False
flag_save = False

if role_user == "admin":

    print("\n")
    print("Menu yang tersedia: ")
    print("- register")
    print("- carirarity")
    print("- caritahun")
    print("- additem")
    print("- hapusitem")
    print("- ubahjumlah")
    print("- riwayatpinjam")
    print("- riwayatkembali")
    print("- riwayatambil")
    print("- help")
    print("- Save")
    print("- Exit")

    choice = input("\nSilahkan pilih menu: ")

    while (not (flag_main)):

        if choice.lower() == "register":
            register(user_log_main)
            choice = input("\nSilahkan pilih menu: ")

        elif choice.lower() == "carirarity":
            gadget_by_rarity(file_path)
            choice = input("\nSilahkan pilih menu: ")

        elif choice.lower() == "caritahun":
            gadget_by_year(file_path)
            choice = input("\nSilahkan pilih menu: ")

        elif choice.lower() == "additem":
            idx = input("Masukkan ID: ")

            if idx[0] == "G":
                if (cek_gadget(gadget_log_main ,idx)):
                    tambah_gadget(idx, gadget_log_main)

            elif idx[0] == "C":
                if (cek_consumable(consumable_log_main, idx)):
                    tambah_consumable(idx, consumable_log_main)

            else:
                print("Gagal menambahkan item karena ID tidak valid.")

            choice = input("\nSilahkan pilih menu: ")

        elif choice.lower() == "hapusitem":
            delete_item(gadget_log_main, consumable_log_main)
            choice = input("\nSilahkan pilih menu: ")

        elif choice.lower() == "ubahjumlah":
            change_item(gadget_log_main, consumable_log_main)
            choice = input("\nSilahkan pilih menu: ")

        elif choice.lower() == "riwayatpinjam":
            tampilkan_gbh(user_log_main, gadget_log_main, borrow_gadget_log_main)
            choice = input("\nSilahkan pilih menu: ")

        elif choice.lower() == "riwayatkembali":
            tampilkan_return_history(user_log_main, gadget_log_main, borrow_gadget_log_main, return_gadget_log_main)
            choice = input("\nSilahkan pilih menu: ")

        elif choice.lower() == "riwayatambil":
            tampilkan_take_consumable(user_log_main, consumable_log_main, take_consumable_log_main)
            choice = input("\nSilahkan pilih menu: ")

        elif choice.lower() == "exit":
            if not (flag_save):
                validasi_save = input("Apakah anda ingin melakukan save? (Y/N):")
                if validasi_save.lower() == "y":
                    save(user_log_main, gadget_log_main, consumable_log_main, borrow_gadget_log_main, take_consumable_log_main, idx_borrow_gadget, idx_take_consumable, return_gadget_log_main)
            print("\nTerima Kasih sudah menggunakan program kami!")
            flag_main = True

        elif choice.lower() == "save":
            save(user_log_main, gadget_log_main, consumable_log_main,borrow_gadget_log_main, take_consumable_log_main, idx_borrow_gadget, idx_take_consumable, return_gadget_log_main)
            flag_save = True
            choice = input("\nSilahkan pilih menu: ")

        elif choice.lower() == "help":
            helpadm(file_path)
            choice = input("\nSilahkan pilih menu: ")

        else:
            print("Menu tidak tersedia. Silahkan input menu yang valid.")
            choice = input("\nSilahkan pilih menu: ")

# Role untuk user
if role_user == "user":

    print("\n")
    print("Menu yang tersedia: ")
    print("- carirarity")
    print("- caritahun")
    print("- pinjam")
    print("- kembalikan")
    print("- minta")
    print("- Save")
    print("- help")
    print("- Exit")
    
    choice = input("\nSilahkan pilih menu: ")

    while (not (flag_main)):

        if choice.lower() == "carirarity":
            gadget_by_rarity(file_path)
            choice = input("\nSilahkan pilih menu: ")

        elif choice.lower() == "caritahun":
            gadget_by_year(file_path)
            choice = input("\nSilahkan pilih menu: ")

        elif choice.lower() == "pinjam":
            borrow_gadget(gadget_log_main, borrow_gadget_log_main, id_user)
            choice = input("\nSilahkan pilih menu: ")

        elif choice.lower() == "minta":
            take_consumable(consumable_log_main, take_consumable_log_main, id_user)
            choice = input("\nSilahkan pilih menu: ")

        elif choice.lower() == "kembalikan":
            return_gadget(gadget_log_main, borrow_gadget_log_main, return_gadget_log_main, id_user)
            choice = input("\nSilahkan pilih menu: ")

        elif choice.lower() == "exit":
            if not (flag_save):
                validasi_save = input("Apakah anda ingin melakukan save? (Y/N):")
                if validasi_save.lower() == "y":
                    save(user_log_main, gadget_log_main, consumable_log_main, borrow_gadget_log_main, take_consumable_log_main, idx_borrow_gadget, idx_take_consumable, return_gadget_log_main)
            print("\nTerima Kasih sudah menggunakan program kami!")
            flag_main = True

        elif choice.lower() == "save":
            save(user_log_main, gadget_log_main, consumable_log_main, borrow_gadget_log_main, take_consumable_log_main, idx_borrow_gadget, idx_take_consumable, return_gadget_log_main)
            flag_save = True
            choice = input("\nSilahkan pilih menu: ")

        elif choice.lower() == "help":
            helpuser(file_path)
            choice = input("\nSilahkan pilih menu: ")
            
        else:
            print("Menu tidak tersedia. Silahkan input menu yang valid.")
            choice = input("\nSilahkan pilih menu: ")