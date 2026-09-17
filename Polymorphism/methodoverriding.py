class animal:
    def bird1(self,name):
        print("animal name:",name)
class bird(animal):
    def bird1(self,name):
        print("bird name:",name)
a=animal()
a.bird1("parrot")
b=bird()
b.bird1("sparrow")

