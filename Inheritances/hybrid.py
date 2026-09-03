class Student:
    def student_info(self):
        print("I am a student")
class Engineering(Student):
    def engineering_info(self):
        print("I am an engineering student")
class Arts(Student):
    def arts_info(self):
        print("I am an arts student")
class Computer(Engineering, Arts):
    def computer_info(self):
        print("I study Computer Science")
s = Computer()
s.student_info()
s.engineering_info()
s.arts_info()
s.computer_info()