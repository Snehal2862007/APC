old = input("old word: ")
new = input("new word: ")
with open("student.txt") as f:
    s = f.read()
with open("student.txt", "w") as f:
    f.write(s.replace(old, new))
