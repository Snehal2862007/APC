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
        self.employee_id = eid
        self.salary = salary

    def display_employee_info(self):
        self.display_person_info()
        print("employee id:", self.employee_id)
        print("salary:", self.salary)

e = Employee("snehal", 21, 101, 30000)
e.display_employee_info()