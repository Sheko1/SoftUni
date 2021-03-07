from .dough import Dough
from .topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, toppings_capacity: int):
        self.__name = name
        self.__toppings_capacity = toppings_capacity
        self.__dough = dough
        self.__toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        self.__toppings_capacity = value

    @property
    def toppings(self):
        return self.__toppings

    @toppings.setter
    def toppings(self, value):
        self.__toppings = value

    def add_topping(self, topping: Topping):
        if len(self.__toppings) == self.__toppings_capacity:
            raise ValueError("Not enough space for another topping")

        elif topping.topping_type not in self.__toppings:
            self.__toppings[topping.topping_type] = 0

        self.__toppings[topping.topping_type] += topping.weight

    def calculate_total_weight(self):
        topping_weight = sum(self.__toppings.values())
        return topping_weight + self.__dough.weight
