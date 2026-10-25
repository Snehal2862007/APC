with open("first.txt") as a, open("second.txt") as b, open("combined.txt", "w") as c:
    c.write(a.read() + "\n" + b.read())
