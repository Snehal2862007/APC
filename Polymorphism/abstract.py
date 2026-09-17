from abc import ABC, abstractmethod
class animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class dog(animal):
    def sound(self):
        return "woof"
class cat(animal):
    def sound(self):
        return "meow"
my_dog = dog()
my_cat = cat()
print(my_dog.sound())
print(my_cat.sound())
