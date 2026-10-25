with open("student.txt") as f:
    s = f.read()
with open("uppercase.txt", "w") as f:
    f.write(s.upper())
