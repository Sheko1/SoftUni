from .animal import Mammal


class Mouse(Mammal):
    WEIGHT_GAINER = 0.10

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if food.__class__.__name__ != "Vegetable" and food.__class__.__name__ != "Fruit":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += Mouse.WEIGHT_GAINER * food.quantity


class Dog(Mammal):
    WEIGHT_GAINER = 0.40

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if food.__class__.__name__ != "Meat":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += Dog.WEIGHT_GAINER * food.quantity


class Cat(Mammal):
    WEIGHT_GAINER = 0.30

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if food.__class__.__name__ != "Meat" and food.__class__.__name__ != "Vegetable":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += Cat.WEIGHT_GAINER * food.quantity


class Tiger(Mammal):
    WEIGHT_GAINER = 1.00

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if food.__class__.__name__ != "Meat":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += Tiger.WEIGHT_GAINER * food.quantity
