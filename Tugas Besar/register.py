from load import *
from parse import *

# Fungsi register akan menerima berbagai input dari user dan akan merubah struktur data user internal
def register(register_log):

    length_reg = len(register_log)

    username = input("Masukkan username: ")
    register_log.append({"id": [], "username": [], "nama": [], "password": [], "alamat": [], "role": "user"})
    register_log[length_reg]["id"] = length_reg
    register_log[length_reg]["username"] = username
    register_log[length_reg]["nama"] = input("Masukkan nama: ")
    register_log[length_reg]["password"] = input("Masukkan password: ")
    register_log[length_reg]["alamat"] = input("Masukkan alamat: ")
    print("User {} telah berhasil register ke dalam Kantong Ajaib.\n".format(username))


