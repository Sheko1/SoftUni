import unittest
from project.train.train import Train


class TestTrain(unittest.TestCase):
    def setUp(self):
        self.train = Train("TestTrain", 10)

    def test_init(self):
        self.assertEqual("TestTrain", self.train.name)
        self.assertEqual(10, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_train_add__when_there_is_no_capacity__expect_value_error(self):
        self.train.capacity = 0
        with self.assertRaises(ValueError) as context:
            self.train.add("test_passenger")

        self.assertEqual("Train is full", str(context.exception))

    def test_train_add__when_passenger_name_is_in_passenger_list__expect_value_error(self):
        self.train.add("test")
        with self.assertRaises(ValueError) as context:
            self.train.add("test")

        self.assertEqual("Passenger test Exists", str(context.exception))

    def test_train_add__expect_to_add_it_and_return_message(self):
        self.assertEqual("Added passenger test", self.train.add("test"))
        self.assertEqual(["test"], self.train.passengers)

    def test_train_remove__when_passenger_not_in_passengers__expect_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.train.remove("test")

        self.assertEqual("Passenger Not Found", str(context.exception))

    def test_train_remove__expect_to_remove_it_and_return_message(self):
        self.train.add("test")
        self.assertEqual("Removed test", self.train.remove("test"))
        self.assertEqual([], self.train.passengers)


if __name__ == '__main__':
    unittest.main()
