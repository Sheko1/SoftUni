from Testing.Exercise.mammal.project.mammal import Mammal
import unittest


class TestMammal(unittest.TestCase):
    name = "TestName"
    mammal_type = "TestType"
    sound = "TestSound"

    def setUp(self):
        self.mammal = Mammal(self.name, self.mammal_type, self.sound)

    def test_mammal_private_attribute(self):
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_mammal_make_sound__expect_correct_values(self):
        self.assertEqual(f"{self.name} makes {self.sound}", self.mammal.make_sound())

    def test_mammal_get_kingdom__expect_correct_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_mammal_info__expect_correct_info(self):
        self.assertEqual(f"{self.name} is of type {self.mammal_type}", self.mammal.info())


if __name__ == '__main__':
    unittest.main()
