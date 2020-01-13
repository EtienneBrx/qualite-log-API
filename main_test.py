import unittest
from main import CoupleOperator


class MainTest(unittest.TestCase):
    def test_sum_tuples_empty(self):
        # liste vide
        cp = CoupleOperator()
        self.assertEqual(0, cp.sum())

    def test_sum_tuples_one_couple(self):
        cp = CoupleOperator()
        cp.add(1,2)
        self.assertEqual(3, cp.sum())

    def test_sum_tuples_one_couple_with_negative(self):
        cp = CoupleOperator()
        cp.add(-6,2)
        self.assertEqual(-4, cp.sum())

    def test_sum_tuples_multiple_tuples(self):
        cp = CoupleOperator()
        cp.add(9, 7)
        cp.add(-6, 2)
        self.assertEqual(12, cp.sum())


if __name__ == '__main__':
    unittest.main()
