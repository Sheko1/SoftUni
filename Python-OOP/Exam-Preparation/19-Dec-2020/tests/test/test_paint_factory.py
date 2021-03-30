from project.factory.paint_factory import PaintFactory
import unittest


class TestPaintFactory(unittest.TestCase):
    def setUp(self):
        self.factory = PaintFactory("Test", 5)

    def test_paint_factory_init__expect_correct_attributes(self):
        self.assertEqual("Test", self.factory.name)
        self.assertEqual(5, self.factory.capacity)
        self.assertEqual({}, self.factory.ingredients)

    def test_paint_factory_add_ingredient__when_not_valid_ingredients_type__expect_type_error(self):
        with self.assertRaises(TypeError) as context:
            self.factory.add_ingredient("test", 2)

        self.assertEqual(f"Ingredient of type test not allowed in PaintFactory", str(context.exception))

    def test_paint_factory_add_ingredient__when_not_enough_capacity__expect_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.factory.add_ingredient("white", 6)

        self.assertEqual("Not enough space in factory", str(context.exception))

    def test_paint_factory_add_ingredient__when_ingredient_not_in_ingredients__expect_to_add_it_with_given_value(self):
        self.assertEqual({}, self.factory.ingredients)
        self.factory.add_ingredient("white", 2)
        self.assertEqual({"white": 2}, self.factory.ingredients)

    def test_paint_factory_add_ingredient__when_ingredient_in_ingredients__expect_to_addition(self):
        self.factory.add_ingredient("white", 2)
        self.factory.add_ingredient("white", 2)
        self.assertEqual({"white": 4}, self.factory.ingredients)

    def test_paint_factory_remove_ingredient__when_ingredient_not_in_ingredients__expect_key_error(self):
        with self.assertRaises(KeyError) as context:
            self.factory.remove_ingredient("test", 2)

        self.assertEqual("'No such ingredient in the factory'", str(context.exception))

    def test_paint_factory_remove_ingredient__when_given_quantity_is_more_than_item_has__expect_value_error(self):
        self.factory.add_ingredient("white", 2)
        with self.assertRaises(ValueError) as context:
            self.factory.remove_ingredient("white", 3)

        self.assertEqual("Ingredients quantity cannot be less than zero", str(context.exception))

    def test_paint_factory_remove_ingredient__when_correct_params__expect_to_subtract_item_quantity(self):
        self.factory.add_ingredient("white", 2)
        self.factory.remove_ingredient("white", 2)
        self.assertEqual({"white": 0}, self.factory.ingredients)

    def test_paint_factory_product_prop__expect_to_return_ingredients(self):
        self.assertEqual({}, self.factory.products)


if __name__ == '__main__':
    unittest.main()
