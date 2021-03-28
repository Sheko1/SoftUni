from cat import Cat
import unittest


class TestCat(unittest.TestCase):
    name = "TestCat"

    def setUp(self):
        self.cat = Cat(self.name)

    def test_cat_eat__expect_size_to_be_increased(self):
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_cat_eat__expect_fed_to_be_true(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_eat__when_fed_is_true__expect_exception(self):
        self.cat.fed = True

        with self.assertRaises(Exception):
            self.cat.eat()

    def test_cat_sleep__when_fed_is_false__expect_exception(self):
        with self.assertRaises(Exception):
            self.cat.sleep()

    def test_cat_sleep__when_sleep__expect_sleepy_to_be_false(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()
