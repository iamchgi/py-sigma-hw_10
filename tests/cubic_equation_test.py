import unittest
from mymath.cubic_equation import cubic_eq_solver

class SquareEqSolverTestCase(unittest.TestCase):
    class SquareEqSolverTestCase(unittest.TestCase):
        def test_no_root(self):
            a = 1
            b = 3
            c = -2
            d = -6
            res = cubic_eq_solver(a, b, c, d)
            '''
            Сформуйте тести для функції обрахунку коренів кубічного рівняння
            Можливо потребуватимуть змін функція, що реалізує обрахунок.
            '''

if __name__ == '__main__':
    unittest.main()