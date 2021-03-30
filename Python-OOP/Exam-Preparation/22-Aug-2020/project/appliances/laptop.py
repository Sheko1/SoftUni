from .appliance import Appliance


class Laptop(Appliance):
    COST = 1

    def __init__(self):
        super().__init__(cost=self.COST)
