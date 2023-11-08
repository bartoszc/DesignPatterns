from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):

    def make_sound(self):
        return "Miau"


class Dog(Animal):

    def make_sound(self):
        return "Hau hau"


class Cow(Animal):

    def make_sound(self):
        return "Mu"


# Testowanie
cat = Cat()
dog = Dog()
cow = Cow()

print(cat.make_sound())  # "Miau"
print(dog.make_sound())  # "Hau hau"
print(cow.make_sound())  # "Mu"
