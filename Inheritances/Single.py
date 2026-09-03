class teacher:
    def __init__(self, name):
        self.name = name
        print(name, "is a teacher")
    def Performances(self):
        grade = int(input("enter the number :"))
        if 1 < grade < 5:
            print("good")
        else:
            print("excellent")
class student(teacher):
    def allocated_teacher(self):
        print(self.name, "is allocated as a teacher")
        self.Performances()
s1 = student("swati")
s1.allocated_teacher()