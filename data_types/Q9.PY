attendance = {
    "monday": {"rahul", "sneha", "amit"},
    "tuesday": {"rahul", "sneha"},
    "wednesday": {"rahul", "sneha", "amit"},
    "thursday": {"rahul", "amit"},
    "friday": {"rahul", "sneha", "amit"}
}
all_students = set.intersection(*attendance.values())
all_attended = set.union(*attendance.values())
one_class = set()
for student in all_attended:
    count = 0
    for students in attendance.values():
        if student in students:
            count += 1
    if count == 1:
        one_class.add(student)
print("students who attended all classes:", all_students)
print("students who attended only one class:", one_class)
print("total unique students:", len(all_attended))