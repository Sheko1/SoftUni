from worker import Worker
import unittest


class WorkerTests(unittest.TestCase):
    name = "Test"
    salary = 50
    energy = 5

    def setUp(self):
        self.worker = Worker(self.name, self.salary, self.energy)

    def test_worker_init__expect_passed_args_to_be_equal_to_attributes(self):
        self.assertEqual(self.name, self.worker.name)
        self.assertEqual(self.salary, self.worker.salary)
        self.assertEqual(self.energy, self.worker.energy)

    def test_worker_rest__expect_energy_to_be_incremented(self):
        self.worker.rest()
        self.assertEqual(self.energy + 1, self.worker.energy)

    def test_worker_work__when_energy_is_0__expect_exception(self):
        self.worker.energy = 0
        with self.assertRaises(Exception):
            self.worker.work()

    def test_worker_work__when_energy_is_above_0__expect_energy_to_be_decreased(self):
        self.worker.work()
        self.assertEqual(self.energy - 1, self.worker.energy)

    def test_worker_work__when_energy_is_above_0__expect_money_to_be_increased_by_salary(self):
        self.worker.work()
        self.assertEqual(self.salary, self.worker.money)

    def test_worker_get_info__expect_correct_values(self):
        expected = f'{self.name} has saved 0 money.'
        self.assertEqual(expected, self.worker.get_info())


if __name__ == '__main__':
    unittest.main()
