class Store:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}
        self.items_filled = 0

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"

    @staticmethod
    def capacity_left(items, capacity):
        return items >= capacity

    @classmethod
    def from_size(cls, name, type, size):
        return cls(name, type, size//2)

    def add_item(self, item_name):
        if self.capacity_left(self.items_filled, self.capacity):
            return "Not enough capacity in the store"

        if item_name not in self.items:
            self.items[item_name] = 0

        self.items[item_name] += 1
        self.items_filled += 1

        return f"{item_name} added to the store"

    def remove_item(self, item, amount):
        if item not in self.items or self.items[item] < amount:
            return f"Cannot remove {amount} {item}"

        self.items[item] -= amount
        self.items_filled -= amount

        return f"{amount} {item} removed from the store"


first_store = Store("First store", "Fruit and Veg", 20)
second_store = Store.from_size("Second store", "Clothes", 500)

print(first_store)
print(second_store)

print(first_store.add_item("potato"))
print(second_store.add_item("jeans"))
print(first_store.remove_item("tomatoes", 1))
print(second_store.remove_item("jeans", 1))
