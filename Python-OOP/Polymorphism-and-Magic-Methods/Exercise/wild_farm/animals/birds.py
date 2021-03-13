from .animal import Bird


class Owl(Bird):
    WEIGHT_GAINER = 0.25

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if food.__class__.__name__ != "Meat":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += Owl.WEIGHT_GAINER * food.quantity


class Hen(Bird):
    WEIGHT_GAINER = 0.35

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        self.food_eaten += food.quantity
        self.weight += Hen.WEIGHT_GAINER * food.quantity
