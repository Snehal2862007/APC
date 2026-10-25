class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print("name:", self.name)
        print("age:", self.age)

class Employee(Person):
    def __init__(self, name, age, eid, salary):
        super().__init__(name, age)
        self.eid = eid
        self.salary = salary

    def display_employee_info(self):
        self.display_person_info()
        print("employee id:", self.eid)
        print("salary:", self.salary)

class Manager(Employee):
    def __init__(self, name, age, eid, salary, department, team_size):
        super().__init__(name, age, eid, salary)
        self.department = department
        self.team_size = team_size

    def display_manager_info(self):
        self.display_employee_info()
        print("department:", self.department)
        print("team size:", self.team_size)

m = Manager("snehal", 21, 101, 50000, "IT", 10)
m.display_manager_info()