filename = input("enter file name: ")

with open(filename, "r") as file:
    content = file.read()
    words = content.split()
    print("total number of words:", len(words))
