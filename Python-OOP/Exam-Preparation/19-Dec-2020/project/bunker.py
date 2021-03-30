from project.medicine.medicine import Medicine
from project.supply.supply import Supply
from project.survivor import Survivor


class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @staticmethod
    def get_last_obj_index_by_type(obj, obj_list):
        index = None
        for i, m in enumerate(obj_list):
            if m.__class__.__name__ == obj.__class__.__name__:
                index = i

        return index

    @property
    def food(self):
        food_to_return = [s for s in self.supplies if s.__class__.__name__ == "FoodSupply"]
        if not food_to_return:
            raise IndexError("There are no food supplies left!")

        return food_to_return

    @property
    def water(self):
        water_to_return = [s for s in self.supplies if s.__class__.__name__ == "WaterSupply"]
        if not water_to_return:
            raise IndexError("There are no water supplies left!")

        return water_to_return

    @property
    def painkillers(self):
        painkillers_to_return = [m for m in self.medicine if m.__class__.__name__ == "Painkiller"]
        if not painkillers_to_return:
            raise IndexError("There are no painkillers left!")

        return painkillers_to_return

    @property
    def salves(self):
        salves_to_return = [m for m in self.medicine if m.__class__.__name__ == "Salve"]
        if not salves_to_return:
            raise IndexError("There are no salves left!")

        return salves_to_return

    def get_medicine_type(self, name):
        if name.lower() == "painkiller":
            return self.painkillers

        else:
            return self.salves

    def get_sustenance_type(self, name):
        if name.lower() == "foodsupply":
            return self.food

        else:
            return self.water

    def add_survivor(self, survivor: Survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")

        self.survivors.append(survivor)

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type: str):
        if not survivor.needs_healing:
            return

        medicine = self.get_medicine_type(medicine_type)
        medicine_to_remove = self.get_last_obj_index_by_type(medicine[0], self.medicine)
        self.medicine.pop(medicine_to_remove)
        medicine[0].apply(survivor)
        return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor: Survivor, sustenance_type: str):
        if not survivor.needs_sustenance:
            return

        supply = self.get_sustenance_type(sustenance_type)
        supply_to_remove = self.get_last_obj_index_by_type(supply[0], self.supplies)
        self.supplies.pop(supply_to_remove)
        supply[0].apply(survivor)
        return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for s in self.survivors:
            s.needs -= s.age * 2
            self.sustain(s, "FoodSupply")
            self.sustain(s, "WaterSupply")
