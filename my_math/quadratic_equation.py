"""
Розрахунок коренів квадратного рівняння
"""
import doctest
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

from create_logger import logger


def square_eq_solver(a, b, c) -> list:
    """
    :param a: Перший коєфіціент квадратного рівняння
    :param b: Другий коєфіціент квадратного рівняння
    :param c: Третій коєфіціент квадратного рівняння
    :return: Коріння (рішення) квадратного рівняння
    >>> square_eq_solver(1,2,3)
    []
    >>> square_eq_solver(0,0,0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError
    >>> square_eq_solver(3,5,3)
    []
    >>> square_eq_solver(3,-3,-3)
    [1.618033988749895, -0.6180339887498949]
    """
    result = []
    discriminant = b * b - 4 * a * c
    logger.debug(f"discriminant: {discriminant}")
    try:
        if discriminant == 0:
            result.append(-b / (2 * a))
        elif discriminant > 0:
            result.append((-b + sqrt(discriminant)) / (2 * a))
            result.append((-b - sqrt(discriminant)) / (2 * a))
        logger.info(f"Коріння у цього рівняння таке: {result}")
        return result
    except ZeroDivisionError:
        logger.warning(f"Divide by zero for argument: {a},{b},{c}")
        raise ZeroDivisionError

def show_result(data) -> None:
    """
    Вівід на консоль результату обчислень
    :param data:
    :return: None
    """
    if len(data) > 0:
        for index, value in enumerate(data):
           print(f'Корень номер {index+1} дорівнює {value:.02f}')
    else:
        print('Рівняння із заданими параметрами не має коренів')

def show_result_image(a, b, c) -> None:
    """
    Графічне зображення функції квадратного рівняння
    :param a: Перший коефіцієнт квадратного рівняння
    :param b: Другий коефіцієнт квадратного рівняння
    :param c: Третій коефіцієнт квадратного рівняння
    :return None
    """
    x = np.linspace(-5, 5, 1000)
    y = a * x ** 2 + b * x + c
    fig, ax = plt.subplots()
    plt.grid(True)
    ax.plot(x, y)
    plt.show()


def quadratic_main():
   # a, b, c = map(int, input('Задайте параметри рівняння ax2 + bx + c через пробіл: a b c: ').split())
   a,b,c = 3, 5, -19
   logger.info("Обчислення ax2 + bx + c=0")
   logger.debug(f"a, b, c = {a, b, c}")
   show_result_image(a, b, c)
   result = square_eq_solver(a, b, c)
   show_result(result)

if __name__ == '__main__':
    doctest.testmod(verbose=True)
