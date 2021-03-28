from Testing.Exercise.vehicle.project.vehicle import Vehicle
import unittest


class VehicleTest(unittest.TestCase):
    fuel = 20
    horse_power = 50

    def setUp(self):
        self.vehicle = Vehicle(self.fuel, self.horse_power)

    def test_vehicle_init__expect_fuel_consumption_to_be_equal_to_default_fuel_consumption(self):
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_vehicle_init__expect_capacity_to_be_equal_to_fuel(self):
        self.assertEqual(self.vehicle.fuel, self.vehicle.capacity)

    def test_vehicle_drive__when_fuel_is_enough__expect_fuel_to_be_decreased(self):
        self.vehicle.drive(5)
        self.assertEqual(13.75, self.vehicle.fuel)

    def test_vehicle_drive__when_fuel_is_not_enough__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.vehicle.drive(20)

        self.assertEqual("Not enough fuel", str(context.exception))

    def test_vehicle_refuel__when_fuel_is_not_above_capacity__expect_fuel_to_be_increased(self):
        self.vehicle.fuel = 5
        self.vehicle.refuel(10)
        self.assertEqual(15, self.vehicle.fuel)

    def test_vehicle_refuel__when_fuel_is_above_capacity__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.vehicle.refuel(1)

        self.assertEqual("Too much fuel", str(context.exception))

    def test_vehicle_str_method(self):
        expect = f"The vehicle has {self.horse_power} " \
               f"horse power with {self.fuel} fuel left and 1.25 fuel consumption"

        self.assertEqual(expect, str(self.vehicle))


if __name__ == '__main__':
    unittest.main()
