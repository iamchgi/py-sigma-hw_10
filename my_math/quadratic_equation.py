"""
Розрахунок коренів квадратного рівняння
"""
import doctest
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

def square_eq_solver(a, b, c) -> list:
    """
     found rezult
    :param a: 
    :param b: 
    :param c: 
    :return:
    >>> square_eq_solver(1, 1, 1)
    1
    >>> square_eq_solver(1, 1, 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: integer division or modulo by zero
    """
    result = []
    discriminant = b * b - 4 * a * c

    if discriminant == 0:
        result.append(-b / (2 * a))
    elif discriminant > 0:
        result.append((-b + sqrt(discriminant)) / (2 * a))
        result.append((-b - sqrt(discriminant)) / (2 * a))

    return result

def show_result(data):
   if len(data) > 0:
       for index, value in enumerate(data):
           print(f'Корень номер {index+1} дорівнює {value:.02f}')
   else:
       print('Рівняння із заданими параметрами не має коренів')

def show_result_image(a, b, c):
    x = np.linspace(-5, 5, 1000)
    y = a * x ** 2 + b * x + c
    fig, ax = plt.subplots()
    plt.grid(True)
    ax.plot(x, y)
    plt.show()


def quadratic_main():
   a, b, c = map(int, input('Задайте параметра рівняння ax2 + bx + c через пробіл: a b c: ').split())
   show_result_image(a, b, c)
   result = square_eq_solver(a, b, c)
   show_result(result)

if __name__ == '__main__':
    doctest.testmod(verbose=True)
    doctest.testfile("quadratic.doctest")
