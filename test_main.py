import unittest
import random
import main
from unittest.mock import patch


class TestMain(unittest.TestCase):

    def test_validate_pos_num_value(self):
        with self.assertRaisesRegex(ValueError, 'Input must be an integer'):
            main.validate_pos_num('a')
            self.assertRaises(TypeError, main.validate_pos_num, -1)
            self.assertRaises(TypeError, main.validate_pos_num, 8.5)

    def test_validate_pos_num_type(self):
        self.assertRaises(TypeError, main.validate_pos_num, 5j + 7)
        self.assertRaises(TypeError, main.validate_pos_num, [6])
        self.assertRaises(TypeError, main.validate_pos_num, [6, 4, 'z'])
        self.assertRaises(TypeError, main.validate_pos_num, {'a', 'b', 'c'})


class TestGetPosInt(unittest.TestCase):
    @patch('builtins.input', return_value='5')
    @patch('builtins.print')
    def test_correct_input_first_attempt(self, mock_print, mock_input):
        self.assertEqual(main.get_positive_int("Enter a positive number: "), 5)

    @patch('builtins.input', side_effect=['not an integer', '10'])
    @patch('builtins.print')
    def test_non_integer_followed_by_correct_input(self, mock_print, mock_input):
        self.assertEqual(main.get_positive_int("Enter a positive number: "), 10)

    @patch('builtins.input', side_effect=['-5', '15'])
    @patch('builtins.print')
    def test_negative_integer_followed_by_correct_input(self, mock_print, mock_input):
        self.assertEqual(main.get_positive_int("Enter a positive number: "), 15)

    @patch('builtins.input', side_effect=['-1', 'abc', '0.5', '20'])
    @patch('builtins.print')
    def test_multiple_invalid_inputs_followed_by_correct_input(self, mock_print, mock_input):
        self.assertEqual(main.get_positive_int("Enter a positive number: "), 20)


class TestValidateRange(unittest.TestCase):
    def test_min_equal_to_max(self):
        self.assertEqual(main.validate_range(10, 10), (10, 10))

    def test_min_less_than_max(self):
        self.assertEqual(main.validate_range(1, 10), (1, 10))

    def test_min_greater_than_max(self):
        self.assertEqual(main.validate_range(10, 1), (1, 10))

    def test_large_values(self):
        self.assertEqual(main.validate_range(100000000, 500000000), (100000000, 500000000))


class TestGetRange(unittest.TestCase):
    @patch('main.get_positive_int')
    def test_get_range(self, mock_get_positive_int):
        mock_get_positive_int.side_effect = [3, 12]
        self.assertEqual(main.get_range(), (3, 12))

        mock_get_positive_int.side_effect = [12, 3]
        self.assertEqual(main.get_range(), (3, 12))


class TestCheckInput(unittest.TestCase):
    def test_with_bigger_random_num(self):
        self.assertEqual(main.check_input(10, 2), (False, 'Enter bigger number'))

    def test_with_smaller_random_num(self):
        self.assertEqual(main.check_input(2, 10), (False, 'Enter smaller number'))

    def test_with_same_nums(self):
        self.assertEqual(main.check_input(2, 2), (True, 'You guessed correctly'))


class TestIntegration(unittest.TestCase):
    @patch('main.get_range', return_value=(0, 10))
    @patch('main.get_positive_int', side_effect=[1, 5, 8, 9, 10])
    def test_with_5_inputs(self, mock_get_range, mock_get_positive_int):
        random.seed(10)
        test_results = ['Enter bigger number',
                        'Enter bigger number',
                        'Enter bigger number',
                        'You guessed correctly']
        self.assertEqual(main.game_loop(), test_results)

    @patch('main.get_range', return_value=(0, 1000))
    @patch('main.get_positive_int', side_effect=[500, 400, 350, 330, 340, 345, 346, 347])
    @patch('random.randint', return_value=347)
    def test_with_8_inputs(self, mock_get_range, mock_get_positive_int, mock_randint):
        test_results = ['Enter smaller number',
                        'Enter smaller number',
                        'Enter smaller number',
                        'Enter bigger number',
                        'Enter bigger number',
                        'Enter bigger number',
                        'Enter bigger number',
                        'You guessed correctly']
        self.assertEqual(main.game_loop(), test_results)
