# f = open("data/users.csv", "a+")
# f.write("\n"+"2;jett;jett;korea;1234;user")
# f.close()

# Using Argparse
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("square", help="square the given number", type=int)
# parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
# args = parser.parse_args()
# answer = args.square**2

# if args.verbose:
#     print("The square of {} is {}".format(args.square, answer))

# else:
#     print(answer)

# from load_gadgets import *

# gadgets = load_gadgets("data/")
# i = 0
# found = False

# while (not (found)) and (i != len(gadgets)):

#     if gadgets[i]["id"] == "G1":
#         gadgets.remove(gadgets[i])
#         found = True

#     i += 1


# with open("data/" + "test.csv", "w") as writer:

#     for i in range(len(gadgets)):

#         idx = gadgets[i]["id"]
#         nama = gadgets[i]["nama"]
#         deskripsi = gadgets[i]["deskripsi"]
#         jumlah = gadgets[i]["jumlah"]
#         rarity = gadgets[i]["rarity"]
#         tahun_ditemukan = gadgets[i]["tahun_ditemukan"]

#         write_value = idx + ";" + nama + ';' + deskripsi + ';' + jumlah + ';' + rarity + ';' + tahun_ditemukan
#         writer.write(write_value + "\n")

from load import *

gadget = load_gadget("21-04-2021/")
borrow_gadget = load_borrow_gadget("21-04-2021/")

for i in range(len(gadget)):
    for j in range(len(borrow_gadget)):
        if gadget[i]["id"] == borrow_gadget[j]["id_gadget"]:
            print(gadget[i])


for i in range(len(gadget)):
    for j in range(len(borrow_gadget)):

        if gadget[i]["id"] == borrow_gadget[j]["id_gadget"]:
            new_jumlah = int(gadget[i]["jumlah"]) - int(borrow_gadget[j]["jumlah"])
            gadget[i]["jumlah"] = str(new_jumlah)
            print(gadget[i])


        
        





