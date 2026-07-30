s = input("enter a string: ")
result = ""
for ch in s:
    if ch != " ":
        result += ch
print("new:", result)