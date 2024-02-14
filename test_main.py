import unittest
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

