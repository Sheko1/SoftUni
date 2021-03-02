class Room:
    def __init__(self, number: int, capacity: int):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    @staticmethod
    def can_take_room(is_taken, capacity, guests):
        return guests <= capacity and not is_taken

    def take_room(self, people):
        if not self.can_take_room(self.is_taken, self.capacity, people):
            return f"Room number {self.number} cannot be taken"

        self.is_taken = True
        self.guests = people

    def free_room(self):
        if not self.is_taken:
            return f"Room number {self.number} is not taken"

        self.is_taken = False
        self.guests = 0
