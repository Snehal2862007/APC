from student.marks import total, percentage
from student.grade import grade
from student.attendance import eligible
m=[80,90,85]
p=percentage(m)
print("total:",total(m),"percentage:",p,"grade:",grade(p),"attendance eligible:",eligible(70,80))
