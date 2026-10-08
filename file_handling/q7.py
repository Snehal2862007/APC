filename = input("enter file name: ")

with open(filename, "r") as file:
    content = file.read()
    print("total number of characters:", len(content))
