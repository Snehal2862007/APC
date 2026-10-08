filename = input("enter file name: ")

with open(filename, "r") as file:
    lines = file.readlines()
    for line in reversed(lines):
        print(line.strip())
