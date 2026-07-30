s = input("enter a string: ")
old = input("enter replace character: ")
new = input("enter new character: ")
result = ""
for ch in s:
    if ch == old:
        result += new
    else:
        result += ch
print("string:", result)