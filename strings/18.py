n = input("Enter the string: ")
new = ""
for i in range(len(n)):
    if i == len(n) - 1 or n[i] != n[i + 1]:
        new += n[i]
print(new)
