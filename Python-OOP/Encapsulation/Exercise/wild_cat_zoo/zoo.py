class Zoo:
    __animals = {"Lion": [], "Tiger": [], "Cheetah": []}
    __workers = {"Keeper": [], "Caretaker": [], "Vet": []}

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.name = name
        self.animals = []
        self.workers = []

    @staticmethod
    def __is_enough_capacity(capacity, obj_list):
        return len(obj_list) < capacity

    @staticmethod
    def __is_enough_budget(budget, price):
        return price <= budget

    @staticmethod
    def __find_worker_by_name(worker_name, obj_list):
        return [obj for obj in obj_list if obj.name == worker_name]

    def add_animal(self, animal, price):
        if not self.__is_enough_capacity(self.__animal_capacity, self.animals):
            return "Not enough space for animal"

        elif not self.__is_enough_budget(self.__budget, price):
            return "Not enough budget"

        Zoo.__animals[animal.animal_type].append(animal)
        self.animals.append(animal)
        self.__budget -= price

        return f"{animal.name} the {animal.animal_type} added to the zoo"

    def hire_worker(self, worker):
        if not self.__is_enough_capacity(self.__workers_capacity, self.workers):
            return "Not enough space for worker"

        self.workers.append(worker)
        Zoo.__workers[worker.worker_type].append(worker)
        return f"{worker.name} the {worker.worker_type} hired successfully"

    def fire_worker(self, worker_name):
        worker = self.__find_worker_by_name(worker_name, self.workers)
        if not worker:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker[0])
        Zoo.__workers[worker[0].worker_type].remove(worker[0])
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        sum_salary = sum([worker.salary for worker in self.workers])
        if not self.__is_enough_budget(self.__budget, sum_salary):
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= sum_salary
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        price = sum([animal.get_needs() for animal in self.animals])
        if not self.__is_enough_budget(self.__budget, price):
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= price
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        result += f"----- {len(Zoo.__animals['Lion'])} Lions:\n"
        result += "\n".join(repr(lion) for lion in Zoo.__animals["Lion"]) + "\n"
        result += f"----- {len(Zoo.__animals['Tiger'])} Tigers:\n"
        result += "\n".join(repr(tiger) for tiger in Zoo.__animals["Tiger"]) + "\n"
        result += f"----- {len(Zoo.__animals['Cheetah'])} Cheetahs:\n"
        result += "\n".join(repr(cheetah) for cheetah in Zoo.__animals["Cheetah"])

        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        result += f"----- {len(Zoo.__workers['Keeper'])} Keepers:\n"
        result += "\n".join(repr(k) for k in Zoo.__workers["Keeper"]) + "\n"
        result += f"----- {len(Zoo.__workers['Caretaker'])} Caretakers:\n"
        result += "\n".join(repr(c) for c in Zoo.__workers["Caretaker"]) + "\n"
        result += f"----- {len(Zoo.__workers['Vet'])} Vets:\n"
        result += "\n".join(repr(v) for v in Zoo.__workers["Vet"])

        return result
