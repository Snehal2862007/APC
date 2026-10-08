filename = input("enter file name: ")

with open(filename, "r") as file:
    for line in file:
        print(line.strip())
