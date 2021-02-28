class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: dict):
        self.ingredients = ingredients
        self.price = price
        self.name = name
        self.ordered = False
        self.ordered_message = f"Pizza {self.name} already prepared and we can't make any changes!"

    def add_extra(self, ingredient: str, quantity: int, ingredient_price: float):
        if self.ordered:
            return self.ordered_message

        if self.ingredients.get(ingredient):
            self.ingredients[ingredient] += quantity
            self.price += ingredient_price

            return

        self.ingredients[ingredient] = quantity
        self.price += quantity * ingredient_price

    def remove_ingredient(self, ingredient: str, quantity: int, ingredient_price: float):
        if self.ordered:
            return self.ordered_message

        if not self.ingredients.get(ingredient):
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"

        elif quantity > self.ingredients[ingredient]:
            return f"Please check again the desired quantity of {ingredient}!"

        self.ingredients[ingredient] -= quantity
        self.price -= quantity * ingredient_price

    def make_order(self):
        self.ordered = True
        return f"You've ordered pizza {self.name} prepared with " \
               f"{', '.join(f'{item}: {quantity}' for item, quantity in self.ingredients.items())}" \
               f" and the price will be {self.price}lv."


margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))
