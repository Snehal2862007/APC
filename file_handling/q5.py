filename = input("enter file name: ")

with open(filename, "r") as file:
    lines = file.readlines()
    print("total number of lines:", len(lines))
