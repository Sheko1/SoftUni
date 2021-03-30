from project.rooms.room import Room
import unittest


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Test", 200, 1)

    def test_room_init_(self):
        self.assertEqual([], self.room.children)
        self.assertEqual("Test", self.room.family_name)
        self.assertEqual(200, self.room.budget)
        self.assertEqual(1, self.room.members_count)
        self.assertEqual(0, self.room.expenses)

    def test_room_expenses__when_expenses_are_negative__expect_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.room.expenses = -1

        self.assertEqual("Expenses cannot be negative", str(context.exception))


if __name__ == '__main__':
    unittest.main()
