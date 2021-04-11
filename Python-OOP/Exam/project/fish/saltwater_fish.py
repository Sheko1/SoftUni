from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    size_to_increase = 2
    initial_size = 5

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, self.initial_size, price)

    def eat(self):
        super().eat()
