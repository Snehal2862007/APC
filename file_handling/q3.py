name = input("enter student name: ")
roll_no = input("enter roll number: ")
branch = input("enter branch: ")
semester = input("enter semester: ")

with open("student.txt", "a") as file:
    file.write(name + "\n")
    file.write(roll_no + "\n")
    file.write(branch + "\n")
    file.write(semester + "\n")
