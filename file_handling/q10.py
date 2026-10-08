filename = input("enter file name: ")
with open(filename, "r") as file:
    content = file.read()
alphabets = 0
digits = 0
spaces = 0
special_chars = 0
for char in content:
    if char.isalpha():
        alphabets += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1
    else:
        special_chars += 1
print("total alphabets:", alphabets)
print("total digits:", digits)
print("total spaces:", spaces)
print("total special characters:", special_chars)
