class Calculator:
    def add(self, a, b, c=0, d=0):
        return a + b + c + d

c = Calculator()

print("two numbers:", c.add(10, 20))
print("three numbers:", c.add(10, 20, 30))
print("four numbers:", c.add(10, 20, 30, 40))