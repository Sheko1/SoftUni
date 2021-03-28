from extended_list import IntegerList
import unittest


class TestIntegerList(unittest.TestCase):
    def test_integer_list_init__when_args_is_not_only_integer__expect_only_integer_to_be_stored(self):
        args = [1, 2, 3, "asd"]
        integer_list = IntegerList(*args)
        self.assertEqual(args[:-1], integer_list.get_data())

    def test_integer_list_add__when_value_is_int__expect_to_add_it_to_the_data_and_return_the_data(self):
        integer_list = IntegerList(1, 2, 3)
        self.assertEqual([1, 2, 3, 4], integer_list.add(4))

    def test_integer_list_add__when_value_is_not_int__expect_value_error(self):
        integer_list = IntegerList(1, 2, 3)

        with self.assertRaises(ValueError):
            integer_list.add("asd")

    def test_integer_list_remove__when_index_is_valid__expect_to_remove_the_value_and_return_it(self):
        integer_list = IntegerList(1, 2, 3)
        self.assertEqual(2, integer_list.remove_index(1))

    def test_integer_list_remove__when_index_is_not_valid__expect_index_error(self):
        integer_list = IntegerList(1, 2, 3)

        with self.assertRaises(IndexError):
            integer_list.remove_index(3)

    def test_integer_list_get__when_index_is_valid__expect_to_return_the_value(self):
        integer_list = IntegerList(1, 2, 3)
        self.assertEqual(3, integer_list.get(2))

    def test_integer_list_get__when_index_is_not_valid__expect_index_error(self):
        integer_list = IntegerList(1, 2, 3)

        with self.assertRaises(IndexError):
            integer_list.get(3)

    def test_integer_list_insert__when_value_is_int_and_index_is_valid__expect_to_add_it_in_data(self):
        integer_list = IntegerList(1, 2, 3)
        integer_list.insert(1, 1)
        self.assertEqual([1, 1, 2, 3], integer_list.get_data())

    def test_integer_list_insert__when_value_is_int_and_index_is_not_valid__expect_index_error(self):
        integer_list = IntegerList(1, 2, 3)

        with self.assertRaises(IndexError):
            integer_list.insert(3, 1)

    def test_integer_list_insert__when_value_is_not_int_and_index_is_valid__expect_value_error(self):
        integer_list = IntegerList(1, 2, 3)

        with self.assertRaises(ValueError):
            integer_list.insert(1, "asd")

    def test_integer_list_get_biggest__expect_to_return_the_biggest_value(self):
        integer_list = IntegerList(1, 10, 3)
        self.assertEqual(10, integer_list.get_biggest())

    def test_integer_list_get_index__expect_to_return_the_index_by_value(self):
        integer_list = IntegerList(1, 2, 3)
        self.assertEqual(1, integer_list.get_index(2))


if __name__ == '__main__':
    unittest.main()
