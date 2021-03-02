class Customer:
    def __init__(self, name: str, age: int, id: int):
        self.age = age
        self.name = name
        self.id = id
        self.rented_dvds = []

    @staticmethod
    def get_dvds_name(dvds):
        return [dvd.name for dvd in dvds]

    def __repr__(self):
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's " \
               f"({', '.join(self.get_dvds_name(self.rented_dvds))})"
