"""
Розрахунок коренів кубічного рівняння^
Метод Кардано — це техніка розв’язування кубічних рівнянь виду ax³ + bx² + cx + d = 0, де a, b, c і d — дійсні коефіцієнти
https://www.wikihow.com/Solve-a-Cubic-Equation
https://www.geeksforgeeks.org/solving-cubic-equations/
"""

import cmath  # бібліотека роботи із комплексними числами
import doctest
import numpy as np
import matplotlib.pyplot as plt
from create_logger import logger


def cubic_eq_solver(a : float, b : float, c : float, d : float) -> list:
    """
    :param a: Перший коєфіціент кубічного рівняння
    :param b: Другий коєфіціент кубічного рівняння
    :param c: Третій коєфіціент кубічного рівняння
    :param d: Четвертий коєфіціент кубічного рівняння
    :return: Коріння (рішення) кубічного рівняння
    >>> cubic_eq_solver(1, 3, -2, -6)
    [(1.414213562373095+0j), (-3-0j), (-1.4142135623730945+0j)]
    >>> cubic_eq_solver(0,0,0,0)
    Traceback (most recent call last):
        ...
    ValueError: Коефіцієнт 'a' не може дорівнювати нулю для кубічного рівняння.
    >>> cubic_eq_solver(1, -3, 3, -1)
    [1.0, 1.0, 1.0]
    >>> cubic_eq_solver(1, -2, 1, 0)
    [(1+0.5773502691896257j), (0.5000000020954758-0.2886751358046364j), (0.49999999790452415-0.28867513338498935j)]
    >>> cubic_eq_solver(1, -6, 11, -6)
    [(3+0j), (1-0j), (1.9999999999999998+0j)]
    """
    if a == 0:
        logger.warning(f"Це не кубічне рівняння {a}x^3+{b}x^2+{c}x+{d}= 0")
        raise ValueError("Коефіцієнт 'a' не може дорівнювати нулю для кубічного рівняння.")
    # calculate intermediate values
    p = (3 * a * c - b ** 2) / (3 * a ** 2)
    q = (2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d) / (27 * a ** 3)

    # Дискримінант
    discriminant = (q / 2) ** 2 + (p / 3) ** 3
    logger.debug(f"discriminant = {discriminant}")

    # Обчислення коренів на основі дискримінанта
    if discriminant > 0:
        # Один дійсний корінь і два - комплексних
        u = (-q / 2 + cmath.sqrt(discriminant)) ** (1 / 3)
        v = (-q / 2 - cmath.sqrt(discriminant)) ** (1 / 3)
        root1 = u + v - b / (3 * a)
        root2 = -(u + v) / 2 - b / (3 * a) + 1j * cmath.sqrt(3) * (u - v) / 2
        root3 = -(u + v) / 2 - b / (3 * a) - 1j * cmath.sqrt(3) * (u - v) / 2
    elif discriminant == 0:
        # Усі корені справжні, хоча б два рівні
        u = (-q / 2) ** (1 / 3)
        root1 = 2 * u - b / (3 * a)
        root2 = -u - b / (3 * a)
        root3 = root2
    else:
        # Усі корені справжні й різні
        r = cmath.sqrt(-p ** 3 / 27)
        phi = cmath.acos(-q / (2 * r))
        u = (2 * (-p / 3) ** 0.5)
        root1 = u * cmath.cos(phi / 3) - b / (3 * a)
        root2 = u * cmath.cos((phi + 2 * cmath.pi) / 3) - b / (3 * a)
        root3 = u * cmath.cos((phi + 4 * cmath.pi) / 3) - b / (3 * a)
    roots = [root1, root2, root3]
    logger.info(f"Коріння у цього рівняння таке: {roots}")
    return roots


def show_result_image(a : float, b : float, c : float, d : float) -> None:
    """
    Графічне зображення функції кубічного рівняння
    :param a: Перший коефіцієнт кубічного рівняння
    :param b: Другий коефіцієнт кубічного рівняння
    :param c: Третій коефіцієнт кубічного рівняння
    :param d: Четвертий коефіцієнт кубічного рівняння
    :return: None
    """
    x = np.linspace(-3, 4, 1000)

    def cubic_eq(x, a, b, c, d):
        return a * x ** 3 + b * x ** 2 + c * x + d

    y = cubic_eq(x, a, b, c, d)
    fig, ax = plt.subplots()
    plt.grid(True)
    ax.plot(x, y)
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')
    plt.show()
    return None


def cubic_main():
    # Define the coefficients of the cubic equation ax^3+bx^2+cx+d
    # a, b, c, d = map(int, input('Задайте параметри рівняння ax^3+bx^2+cx+d через пробіл: a b c d: ').split())
    # a, b, c, d = 1, 3, -2, -6  # 1.4 3 1.4
    # a, b, c, d = 1, -3, 3, -1 # 1 1 1
    # a, b, c, d = 1, -2, 1, 0 # 1 1 0
    # a, b, c, d = 1, -3, 0, 4  # 2 2 -1
    a, b, c, d = -1, -3, 0, -4 # -3.3553014+0.j          0.1776507+1.07730381j  0.1776507-1.07730381j
    # a, b, c, d = 1, -6, 11, -6 # 3, 1, 2
    logger.info("Обчислення ax^3+bx^2+cx+d=0")
    logger.debug(f"a, b, c, d = {a, b, c, d}")
    root = cubic_eq_solver(a, b, c, d)
    show_result_image(a, b, c, d)

    print("y1 =", (a * root[0] ** 3) + (b * root[0] ** 2) + c * root[0] + d)
    print("y2 =", (a * root[1] ** 3) + (b * root[1] ** 2) + c * root[1] + d)
    print("y3 =", (a * root[2] ** 3) + (b * root[2] ** 2) + c * root[2] + d)

    # roots of cubic equation - test solution
    p = [a, b, c, d]
    roots = np.roots(p)
    print('test solution_1 = ', roots)

    p = np.poly1d([a, b, c, d])
    root = p.r
    print('test solution_2 = ', root)


if __name__ == '__main__':
    doctest.testmod(verbose=True)
