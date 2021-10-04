from parse import *

def load_user(file):

    user = []

    with open(file + "user.csv", "r") as reader:
        for lines in reader:
            temp_arr = parse(lines, ";")
            temp_dict = {}
            temp_dict["id"] = temp_arr[0]
            temp_dict["username"] = temp_arr[1]
            temp_dict["nama"] = temp_arr[2]
            temp_dict["password"] = temp_arr[3]
            temp_dict["alamat"] = temp_arr[4]
            temp_dict["role"] = temp_arr[5].replace("\n", "")
            user.append(temp_dict)

    return user

