from load import *

# Fungsi login mengembalikan value berupa tuple yang berisi boolean untuk menandakan keberhasilan login,
# role user saat login yang akan dicek dari user.csvnya, dan juga id user saat login
def login(file):

    user =  load_user(file)
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    i = 0               # inisialisasi untuk loop
    found = False

    while (not(found)) and (i != len(user)):

        if (user[i]["username"] == username) and (user[i]["password"] == password):
            print("Login berhasil\n")
            found = True
            return (found, user[i]["role"],user[i]["id"])
        
        else:
            i += 1
    
    if (not (found)):
        print("Login gagal! Silahkan coba lagi\n")
        return (found, "user", "0")
        
# print(login("data/"))