class Child:
    def __init__(self, food_cost: int, *toys_cost):
        self.cost: float = food_cost + sum(toys_cost)

    @property
    def month_cost(self):
        return self.cost * 30
