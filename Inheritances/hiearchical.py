class Student:
    def student_info(self):
        print("he is a student")
class Engineering(Student):
    def engineering_info(self,college):
        print("he pursue engineering ")
        print(college,"is best")
class Medical(Student):
    def medical_info(self,hospital_name):
        print("I am a medical student")
        print(hospital_name,"is a hospital where i work")

e = Engineering()
e.student_info()
e.engineering_info("DYPCET")
m = Medical()
m.medical_info("D.Y.Patil Hospital")