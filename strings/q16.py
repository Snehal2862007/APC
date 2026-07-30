n = input("Enter the string: ")
new = ""
for ch in n:
    if ch not in new:
        count = 0
        for c in n:
            if ch == c:
                count += 1
        print(ch, ":", count)
        new += ch