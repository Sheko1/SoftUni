from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        result = 0
        for room in self.rooms:
            result += room.expenses + room.room_cost

        return f"Monthly consumption: {result:.2f}$."

    def pay(self):
        result = []

        for room in self.rooms:
            if room.budget < room.expenses + room.room_cost:
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(room)
                continue

            room.budget -= room.expenses + room.room_cost
            result.append(f"{room.family_name} paid {room.expenses + room.room_cost:.2f}$ and have "
                          f"{room.budget:.2f}$ left.")

        return "\n".join(result)

    def status(self):
        result = [f"Total population: {sum(r.members_count for r in self.rooms)}"]

        for room in self.rooms:
            result.append(f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, "
                          f"Expenses: {room.expenses:.2f}$")

            for i, child in enumerate(room.children):
                result.append(f"--- Child {i + 1} monthly cost: {child.month_cost:.2f}$")

            if room.appliances:
                result.append(f"--- Appliances monthly cost: "
                              f"{sum(item.get_monthly_expense() for item in room.appliances):.2f}$")

        return "\n".join(result)
