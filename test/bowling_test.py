import unittest
from app.bowling import BowlingGame, check_input


class BowlingGameTest(unittest.TestCase):
    def test_check_input_invalid_bounds(self):
        result = check_input(-6)
        self.assertFalse(result)

        result = check_input(11)
        self.assertFalse(result)

    def test_check_input_invalid_type(self):
        result = check_input('A')
        self.assertFalse(result)

        result = check_input("test")
        self.assertFalse(result)

    def test_check_input_valid(self):
        result = check_input(4)
        self.assertTrue(result)

    def test_check_input_valid_bounds(self):
        result = check_input(0)
        self.assertTrue(result)

        result = check_input(10)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()

