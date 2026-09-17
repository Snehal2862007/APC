class calculator:
    def add(self, first, second):
        return first + second
    def addthree(self,first,second,third):
        return first+second+third
    
calc = calculator()
print(calc.add(2, 3))
print(calc.addthree(2, 3, 4))
