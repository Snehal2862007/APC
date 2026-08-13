student = []
grades = []
def add_student(name, grade):
    student.append(name)
    grades.append(grade)
    print("Student added successfully.")
def update_grade(name, new_grade):
    if name in student:
        index = student.index(name)
        grades[index] = new_grade
        print("Grade updated successfully.")
    else:
        print("Student not found.")
def remove_student(name):
    if name in student:
        index = student.index(name)
        student.pop(index)
        grades.pop(index)
        print("Student removed successfully.")
    else:
        print("Student not found.")
def average_grade():
    if len(grades) == 0:
        print("No students.")
    else:
        result = sum(grades) / len(grades)
        print("Average Grade:", result)
def max_min_grade():
    if len(grades) == 0:
        print("No students.")
    else:
        highest = max(grades)
        lowest = min(grades)
        print("Highest Grade:", highest)
        print("Lowest Grade:", lowest)
def display():
    if len(student) == 0:
        print("No students.")
    else:
        print("\nStudent List")
        for i in range(len(student)):
            print(student[i], "=", grades[i])
while True:
    print("Student Grade Management System")
    print("1. Add Student")
    print("2. Update Grade")
    print("3. Remove Student")
    print("4. Calculate Average Grade")
    print("5. Display Highest and Lowest Grade")
    print("6. Display All Students")
    print("7. Exit")
    choice = int(input("Enter the choice: "))
    if choice == 1:
        name = input("Enter student name: ")
        grade = int(input("Enter marks: "))
        add_student(name, grade)
    elif choice == 2:
        name = input("Enter student name: ")
        new_grade = int(input("Enter new marks: "))
        update_grade(name, new_grade)
    elif choice == 3:
        name = input("Enter student name: ")
        remove_student(name)
    elif choice == 4:
        average_grade()
    elif choice == 5:
        max_min_grade()
    elif choice == 6:
        display()
    elif choice == 7:
        print("Exiting...")
        break
    else:
        print("Invalid choice.")