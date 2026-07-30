n = input("Enter the string: ")
new = ""
for i in range(len(n) - 1):
    if n[i] == n[i + 1]:
        if len(new) == 0 or new[-1] != n[i]:
            new += n[i]
print(new)
