class Zoo:
    _animal = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammal = []
        self.fish = []
        self.bird = []

    def add(self, type_animal, name):
        if type_animal == "mammal":
            self.mammal.append(name)
            zoo._animal += 1

        elif type_animal == "fish":
            self.fish.append(name)
            zoo._animal += 1

        elif type_animal == "bird":
            self.bird.append(name)
            zoo._animal += 1

    def get_info(self, type_animal):
        result = ""
        if type_animal == "mammal":
            result += f"Mammals in {self.zoo_name}: {', '.join(self.mammal)}\n"

        elif type_animal == "fish":
            result += f"Fishes in {self.zoo_name}: {', '.join(self.fish)}\n"

        elif type_animal == "bird":
            result += f"Birds in {self.zoo_name}: {', '.join(self.bird)}\n"

        result += f"Total animals: {self._animal}"

        return result


zoo_n = input()
animals = int(input())

zoo = Zoo(zoo_n)

for i in range(animals):
    animal = input()
    data = animal.split(" ", maxsplit=1)
    zoo.add(data[0], data[1])

command = input()
print(zoo.get_info(command))
