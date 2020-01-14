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

    def test_sum_tuples_multiple_tuples(self):
        cp = CoupleOperator()
        cp.add(3, 5)
        cp.add(6, 2)
        self.assertEqual(16, cp.sum())

    def test_sum_with_couple_equal_ten(self):
        cp = CoupleOperator()
        cp.add(5, 5)
        cp.add(6, 3)
        self.assertEqual(25, cp.sum())

    def test_sum_with_first_number_ten(self):
        cp = CoupleOperator()
        cp.add(10, 0)
        cp.add(6, 3)
        self.assertEqual(28, cp.sum())

    def test_sum_with_second_number_ten(self):
        cp = CoupleOperator()
        cp.add(0, 10)
        cp.add(6, 3)
        self.assertEqual(25, cp.sum())

    def test_sum_one_couple_spare(self):
        cp = CoupleOperator()
        cp.add(7, 3)
        self.assertEqual(10, cp.sum())

    def test_sum_one_couple_strike(self):
        cp = CoupleOperator()
        cp.add(10, 0)
        self.assertEqual(10, cp.sum())

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

    def test_add_more_than_ten(self):
        cp = CoupleOperator()
        for i in range(10):
            cp.add(0, 1)
        self.assertEqual(10, len(cp.tuples))
        with self.assertRaises(Exception) as context:
            cp.add(0, 1)
        self.assertEqual(10, len(cp.tuples))

    def test_add_negative_number(self):
        cp = CoupleOperator()
        with self.assertRaises(Exception) as context:
            cp.add(0, -9)
        with self.assertRaises(Exception) as context:
            cp.add(-9, 0)
        with self.assertRaises(Exception) as context:
            cp.add(-10, -20)
        self.assertEqual(0, len(cp.tuples))

    def test_add_bounds(self):
        cp = CoupleOperator()
        cp.add(0, 0)
        self.assertEqual(1, len(cp.tuples))
        cp.add(9, 1)
        self.assertEqual(2, len(cp.tuples))

    def test_add_with_sum_more_than_ten(self):
        cp = CoupleOperator()
        with self.assertRaises(Exception) as context:
            cp.add(15, 5)
        self.assertEqual(0, len(cp.tuples))

    def test_add_with_real_values(self):
        cp = CoupleOperator()
        with self.assertRaises(Exception) as context:
            cp.add(3.5, 5)
        self.assertEqual(0, len(cp.tuples))

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
