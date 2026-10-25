def total(marks):
    return sum(marks)

def percentage(marks):
    return total(marks) / 5

def grade(per):
    if per >= 75:
        return "a"
    elif per >= 60:
        return "b"
    elif per >= 40:
        return "c"
    return "fail"

students = {}

n = int(input("enter number of students: "))

for i in range(n):
    name = input("enter name: ")
    roll = input("enter roll number: ")
    marks = []
    for j in range(5):
        marks.append(float(input("enter marks: ")))
    students[roll] = [name, marks]

for roll, data in students.items():
    marks = data[1]
    per = percentage(marks)
    print(roll, data[0], total(marks), per, grade(per))

if students:
    avg = sum(percentage(s[1]) for s in students.values()) / len(students)
    highest = max(students, key=lambda x: total(students[x][1]))
    lowest = min(students, key=lambda x: total(students[x][1]))

    print("class average:", avg)
    print("highest scorer:", students[highest][0])
    print("lowest scorer:", students[lowest][0])