import unittest
from main import CoupleOperator


class MainTest(unittest.TestCase):
    def test_sum_tuples_empty(self):
        # liste vide
        cp = CoupleOperator()
        self.assertEqual(0, cp.sum())

    def test_sum_tuples_one_couple(self):
        cp = CoupleOperator()
        cp.add(1, 2)
        self.assertEqual(3, cp.sum())

    def test_sum_tuples_one_couple_with_negative(self):
        cp = CoupleOperator()
        cp.add(-6, 2)
        self.assertEqual(-4, cp.sum())

    def test_sum_tuples_multiple_tuples(self):
        cp = CoupleOperator()
        cp.add(9, 7)
        cp.add(-6, 2)
        self.assertEqual(12, cp.sum())

    def test_add(self):
        cp = CoupleOperator()
        cp.add(1, 0)
        self.assertEqual(1, len(cp.tuples))
        self.assertEqual((1, 0), cp.tuples[0])

    def test_add_multiple(self):
        cp = CoupleOperator()
        cp.add(0, 1)
        cp.add(2, 3)
        cp.add(4, 5)
        self.assertEqual(3, len(cp.tuples))
        self.assertEqual((0, 1), cp.tuples[0])
        self.assertEqual((2, 3), cp.tuples[1])
        self.assertEqual((4, 5), cp.tuples[2])

    def test_pop(self):
        cp = CoupleOperator()
        cp.add(0, 1)
        cp.add(2, 3)
        cp.pop()
        self.assertEqual(1, len(cp.tuples))
        self.assertEqual((0, 1), cp.tuples[0])

    def test_pop_empty_list(self):
        cp = CoupleOperator()
        self.assertRaises(IndexError, cp.pop)


if __name__ == '__main__':
    unittest.main()
