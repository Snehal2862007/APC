filename = input("enter file name: ")
with open(filename, "r") as file:
    content = file.read().lower()
vowels = "aeiou"
v_count = 0
c_count = 0
for char in content:
    if char.isalpha():
        if char in vowels:
            v_count += 1
        else:
            c_count += 1
print("total vowels:", v_count)
print("total consonants:", c_count)
