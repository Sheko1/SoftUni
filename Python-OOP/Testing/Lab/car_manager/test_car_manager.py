from car_manager import Car
import unittest


class TestCar(unittest.TestCase):
    make = "TestMake"
    model = "TestModel"
    fuel_consumption = 5
    fuel_capacity = 20

    def setUp(self):
        self.car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)

    def test_car_make__when_value_is_not_none__expect_to_change_make(self):
        self.car.make = "test"
        self.assertEqual("test", self.car.make)

    def test_car_make__when_value_is_none__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.make = None
        self.assertEqual("Make cannot be null or empty!", str(context.exception))

    def test_car_model__when_value_is_not_none__expect_to_change_model(self):
        self.car.model = "test"
        self.assertEqual("test", self.car.model)

    def test_car_model__when_value_is_none__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.model = None
        self.assertEqual("Model cannot be null or empty!", str(context.exception))

    def test_car_fuel_consumption__when_value_is_above_0__expect_to_change_fuel_consumption(self):
        self.car.fuel_consumption = 2
        self.assertEqual(2, self.car.fuel_consumption)

    def test_car_fuel_consumption__when_value_is_0__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(context.exception))

    def test_car_fuel_consumption__when_value_is_below_0__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_consumption = -1
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(context.exception))

    def test_car_fuel_capacity__when_value_is_above_0__expect_to_change_fuel_capacity(self):
        self.car.fuel_capacity = 2
        self.assertEqual(2, self.car.fuel_capacity)

    def test_car_fuel_capacity__when_value_is_0__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(context.exception))

    def test_car_fuel_capacity__when_value_is_below_0__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_capacity = -1
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(context.exception))

    def test_car_fuel_amount__when_value_is_above_0__expect_to_change_fuel_amount(self):
        self.car.fuel_amount = 2
        self.assertEqual(2, self.car.fuel_amount)

    def test_car_fuel_amount__when_value_is_below_0__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(context.exception))

    def test_car_refuel__when_fuel_is_above_0_and_fuel_amount_is_not_above_fuel_capacity__expect_to_add_value_to_fuel_amount(
            self):
        self.car.refuel(5)
        self.assertEqual(5, self.car.fuel_amount)

    def test_car_refuel__when_fuel_is_above_0_and_fuel_amount_is_above_fuel_capacity__expect_fuel_amount_and_fuel_capacity_to_be_equal(
            self):
        self.car.refuel(21)
        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test_car_refuel__when_value_is_0__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(context.exception))

    def test_car_refuel__when_value_is_below_0__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.refuel(-1)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(context.exception))

    def test_car_drive__when_fuel_amount_is_enough__expect_fuel_amount_to_be_decreased(self):
        self.car.fuel_amount = 5
        self.car.drive(100)
        self.assertEqual(0, self.car.fuel_amount)

    def test_car_drive__when_fuel_amount_is_not_enough__expect_exception(self):
        self.car.fuel_amount = 4
        with self.assertRaises(Exception) as context:
            self.car.drive(100)
        self.assertEqual("You don't have enough fuel to drive!", str(context.exception))


if __name__ == '__main__':
    unittest.main()
