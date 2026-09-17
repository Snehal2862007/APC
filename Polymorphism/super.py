class parent:
    def __init__(self, name):
        self.name = name
class child(parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    def display(self):
        print(self.name)
        print(self.age)
a=child("snehal", 20)
a.display()
