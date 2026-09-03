class Employee:
    def __init__(self,name):
        self.name=name
    def employee_info(self,name):
        print(name,"is an employee")
class Manager(Employee):
    def manager_info(self,name):
        self.name
        print(name,"is manager")
class Developer(Manager):
    def developer_info(self,name):
        self.name=name
        print(name,"is a developer")
d1 = Developer("riya")
d1.employee_info("ketaki")
d1.manager_info("snehal")
d1.developer_info("Yash")