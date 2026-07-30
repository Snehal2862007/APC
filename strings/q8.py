s = input("Enter a string: ")
ch = input("Enter the character to find: ")
count = 0
for c in s:
    if c == ch:
        count += 1
print("Frequency of", ch, "is", count)