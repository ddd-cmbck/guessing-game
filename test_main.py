import unittest
import main


class TestMain(unittest.TestCase):

    def test_validate_pos_num_value(self): # to do more tests
        with self.assertRaisesRegex(ValueError, 'Input must be an integer'):
            main.validate_pos_num('a')

