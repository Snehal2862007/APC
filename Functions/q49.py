students = [("ram", 80), ("sita", 90), ("shyam", 60)]

def average(students):
    return sum(map(lambda x: x[1], students)) / len(students)

above = list(filter(lambda x: x[1] > 75, students))
ordered = sorted(students, key=lambda x: x[1])

print("average:", average(students))
print("above 75:", above)
print("sorted:", ordered)