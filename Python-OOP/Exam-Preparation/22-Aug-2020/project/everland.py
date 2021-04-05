from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        result = sum((room.expenses + room.room_cost) for room in self.rooms)
        return f"Monthly consumption: {result:.2f}$."

    def pay(self):
        result = []
        index = 0

        while index < len(self.rooms):
            room = self.rooms[index]
            if room.budget < room.expenses + room.room_cost:
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.pop(index)
                continue

            room.budget -= (room.expenses + room.room_cost)
            result.append(f"{room.family_name} paid {room.expenses + room.room_cost:.2f}$ "
                          f"and have {room.budget:.2f}$ left.")
            index += 1

        return "\n".join(result)

    def status(self):
        result = [f"Total population: {sum(room.members_count for room in self.rooms)}"]

        for room in self.rooms:
            result.append(f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$"
                          f", Expenses: {room.expenses:.2f}$")

            for index, child in enumerate(room.children):
                result.append(f"--- Child {index + 1} monthly cost: {child.get_monthly_expense():.2f}$")

            if hasattr(room, "appliances"):
                result.append(f"--- Appliances monthly cost: {room.calculate_expenses(room.appliances):.2f}$")

        return "\n".join(result)
