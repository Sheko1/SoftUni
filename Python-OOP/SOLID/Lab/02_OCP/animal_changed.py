from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        return "meow"


class Dog(Animal):
    def make_sound(self):
        return "woof-woof"


class Chicken(Animal):
    def make_sound(self):
        return "cluck"


def animal_sound(animals: list[Animal]):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat(), Dog(), Chicken()]
animal_sound(animals)
