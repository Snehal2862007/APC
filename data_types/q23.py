import re

with open("input.txt", "r") as f:
    text = f.read()

old = input("enter word to find: ")
new = input("enter replacement: ")
choice = input("ignore case? yes/no: ")

if old:
    if choice.lower() == "yes":
        text = re.sub(re.escape(old), lambda m: new, text, flags=re.IGNORECASE)
    else:
        text = text.replace(old, new)

with open("output.txt", "w") as f:
    f.write(text)

print("text replaced and saved in output.txt")