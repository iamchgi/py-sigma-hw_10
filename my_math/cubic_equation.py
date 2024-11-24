"""
Розрахунок коренів кубічного рівняння^
Метод Кардано — це техніка розв’язування кубічних рівнянь виду ax³ + bx² + cx + d = 0, де a, b, c і d — дійсні коефіцієнти
https://www.wikihow.com/Solve-a-Cubic-Equation
https://www.geeksforgeeks.org/solving-cubic-equations/
"""

import cmath            # бібліотека роботи із комплексними числами
import numpy as np
import matplotlib.pyplot as plt


def cubic_eq_solver(a, b, c, d):

    # calculate intermediate values
    p = (3 * a * c - b ** 2) / (3 * a ** 2)
    q = (2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d) / (27 * a ** 3)
    delta = (q ** 2 / 4 + p ** 3 / 27)
    print("delta:", delta)

    # determine number and type of roots
    if delta > 0:  # one real and two complex roots
        u = (-q / 2 + cmath.sqrt(delta)) ** (1 / 3)
        v = (-q / 2 - cmath.sqrt(delta)) ** (1 / 3)
        x1 = u + v - b / (3 * a)
        x2 = -(u + v) / 2 - b / (3 * a) + (u - v) * cmath.sqrt(3) / 2j
        x3 = -(u + v) / 2 - b / (3 * a) - (u - v) * cmath.sqrt(3) / 2j
        print("One real root and two complex roots:")
        print("x1 = ", x1.real)
        print("x2 = ", x2)
        print("x3 = ", x3)

    elif delta == 0:  # three real roots, two are equal
        '''
        Тестами виявіть / доведіть: чи спрацьовує ця гілка та чи вірна вона?
        '''
        u = (-q / 2) ** (1 / 3)
        v = u
        x1 = 2 * u - b / (3 * a)
        x2 = -u - b / (3 * a)
        print("Three real roots, two are equal:")
        print("x1 = ", x1.real)
        print("x2 = ", x2.real)
        print("x3 = ", x3.real)

    else:  # three distinct real roots
        u = (-q / 2 + cmath.sqrt(delta)) ** (1 / 3)
        v = (-q / 2 - cmath.sqrt(delta)) ** (1 / 3)
        x1 = u + v - b / (3 * a)
        x2 = -(u + v) / 2 - b / (3 * a) + (u - v) * cmath.sqrt(3) / 2j
        x3 = -(u + v) / 2 - b / (3 * a) - (u - v) * cmath.sqrt(3) / 2j
        print("Three distinct real roots:")
        print("x1 = ", x1.real)
        print("x2 = ", x2.real)
        print("x3 = ", x3.real)

    print("y1 =", (a * x1 ** 3) + (b * x1 ** 2) + c * x1 + d)
    print("y2 =", (a * x2 ** 3) + (b * x2 ** 2) + c * x2 + d)
    print("y3 =", (a * x3 ** 3) + (b * x3 ** 2) + c * x3 + d)

    x = np.linspace(-3, 4, 1000)

    def cubic_eq(x, a, b, c, d):

        return a * x ** 3 + b * x ** 2 + c * x + d

    y = cubic_eq(x, a, b, c, d)

    fig, ax = plt.subplots()
    ax.plot(x, y)

    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')

    plt.show()

def cubic_main():
    # Define the coefficients of the cubic equation ax^3+bx^2+cx+d

    a = 1
    b = 3
    c = -2
    d = -6

    # Тести мають виявити і таке неподобство - спонукає до модифікації коду
    # a = 0
    # b = 0
    # c = 0
    # d = 0

    cubic_eq_solver(a, b, c, d)

    # roots of cubic equation - test solution
    p = [a, b, c, d]
    roots = np.roots(p)
    print('test solution_1 = ', roots)

    p = np.poly1d([a, b, c, d])
    root = p.r
    print('test solution_2 = ', root)

if __name__ == '__main__':
    cubic_main()


