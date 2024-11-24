import unittest
from my_math.cubic_equation import cubic_eq_solver


class SquareEqSolverTestCase(unittest.TestCase):
    def test_one_root_two_equal(self):
        a, b, c, d = 1, -3, 0, 4  # 2 2 -1
        res = cubic_eq_solver(a, b, c, d)
        self.assertEqual(res, [(2 + 1.7320508075688772j), (0.4999999999999999 - 0.8660254037844386j),
                               (0.4999999999999999 - 0.8660254037844386j)])

    def test_three_root(self):
        a, b, c, d = 1, 3, -2, -6  # 1.4 3 1.4
        res = cubic_eq_solver(a, b, c, d)
        self.assertEqual(len(res), 3)
        self.assertEqual(res, [(1.414213562373095 + 0j), (-3 - 0j), (-1.4142135623730945 + 0j)])

    def test_value_error(self):
        a, b, c, d = 0, 0, 0, 0
        with self.assertRaises(ValueError):
            cubic_eq_solver(a, b, c, d)

    def test_one_root_two_equal_second_case(self):
        a, b, c, d = -1, -3, 0, -4 #-3.3553014+0.j          0.1776507+1.07730381j  0.1776507-1.07730381j
        res = cubic_eq_solver(a, b, c, d)
        self.assertEqual(res, [(0.17765069880406004+2.0397508438976244j),(-0.6558528798801239-1.5585273283737948j),
                               (-2.521797818923936-0.4812235155238296j)])

    def test_three_root_second_case(self):
        a, b, c, d = 1, -3, 3, -1  # 1 1 1
        res = cubic_eq_solver(a, b, c, d)
        self.assertEqual(res, [1, 1, 1])

    def test_one_root_two_equal_second(self):
        a, b, c, d = 1, -2, 1, 0  # 1 1 0
        res = cubic_eq_solver(a, b, c, d)
        self.assertEqual(res, [(1 + 0.5773502691896257j), (0.5000000020954758 - 0.2886751358046364j),
                               (0.49999999790452415 - 0.28867513338498935j)])

    def test_three_roots(self):
        a, b, c, d = 1, -6, 11, -6  # 3, 1, 2
        res = cubic_eq_solver(a, b, c, d)
        self.assertEqual(res, [(3 + 0j), (1 - 0j), (1.9999999999999998 + 0j)])


if __name__ == '__main__':
    unittest.main()
