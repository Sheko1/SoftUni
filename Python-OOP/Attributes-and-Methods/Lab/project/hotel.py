class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @staticmethod
    def find_room_by_room_number(rooms, room_number):
        for room in rooms:
            if room.number == room_number:
                return room

    @staticmethod
    def sorted_rooms(rooms):
        return [str(room.number) for room in rooms if not room.is_taken], [str(room.number) for room in rooms if
                                                                           room.is_taken]

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = self.find_room_by_room_number(self.rooms, room_number)
        result = room.take_room(people)

        if result:
            return result

        self.guests += people

    def free_room(self, room_number):
        room = self.find_room_by_room_number(self.rooms, room_number)
        guest_to_remove = room.guests
        result = room.free_room()

        if result:
            return result

        self.guests -= guest_to_remove

    def print_status(self):
        free_rooms, taken_rooms = self.sorted_rooms(self.rooms)
        print(f"Hotel {self.name} has {self.guests} total guests\nFree rooms: {', '.join(free_rooms)}\nTaken rooms:"
              f" {', '.join(taken_rooms)}")
