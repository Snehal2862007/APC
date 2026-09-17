class cat:
    def sound(self):
        return "meow"
class dog:
    def sound(self):
        return "woof"
def make_sound(animal):
    print(animal.sound())
my_cat = cat()
my_dog = dog()
make_sound(my_cat)
make_sound(my_dog)
