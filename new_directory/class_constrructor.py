class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    def __del__(self):
        print("destructor called")
    def display_info(self):
        print(f"Car Brand: {self.brand}, Year: {self.year}")

car1 = Car("Toyota", 2022)
car2 = Car("Tesla", 2026)
car1.display_info()
car2.display_info()
del car1
