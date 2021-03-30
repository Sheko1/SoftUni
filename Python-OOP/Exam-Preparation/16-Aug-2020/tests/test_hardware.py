from unittest import TestCase
from project.hardware.hardware import Hardware
from project.software.software import Software


class TestHardware(TestCase):
    def setUp(self):
        self.hardware = Hardware("TestHardware", "TestType", 10, 10)
        self.software = Software("TestSoftware", "TestType", 10, 10)

    def test_hardware_install__when_software_capacity_is_above_hardware_capacity__expept_exception(self):
        self.software.capacity_consumption += 1
        with self.assertRaises(Exception) as context:
            self.hardware.install(self.software)

        self.assertEqual("Software cannot be installed", str(context.exception))

    def test_hardware_install__when_software_memory_is_above_hardware_memory__expept_exception(self):
        self.software.memory_consumption += 1
        with self.assertRaises(Exception) as context:
            self.hardware.install(self.software)

        self.assertEqual("Software cannot be installed", str(context.exception))

    def test_hardware_install__when_software_memory_and_capacity_is_above_hardware_memory_and_capacity_expect_exception(
            self):
        self.software.memory_consumption += 1
        self.software.capacity_consumption += 1

        with self.assertRaises(Exception) as context:
            self.hardware.install(self.software)

        self.assertEqual("Software cannot be installed", str(context.exception))

    def test_hardware_install__when_software_consumption_is_valid__expect_to_add_it_in_software_components(self):
        self.hardware.install(self.software)
        self.assertEqual([self.software], self.hardware.software_components)

    def test_hardware_uninstall__expect_software_to_be_removed_from_software_components(self):
        self.hardware.install(self.software)
        self.hardware.uninstall(self.software)
        self.assertEqual([], self.hardware.software_components)
