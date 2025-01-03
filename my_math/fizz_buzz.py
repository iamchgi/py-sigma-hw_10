"""
Виконав: Григорій Чернолуцький
Модуль
роботи з алгоритмом FizzBuzz.

Логіка роботи алгоритму:
На вхід алгоритму подається деяке число n – набране із клавіатури, або задане
множиною. Необхідно сформувати вихідну послідовність, що відповідає властивостям числа n:
якщо число можна поділити на 3 без залишку, замість числа буде виведено Fizz.
якщо число ділиться на 5 без залишку, результат відображатиме Buzz замість числа.
якщо дане число ділиться і на 3, і на 5, замість числа буде надруковано FizzBuzz.
якщо число не можна поділити на 3 або 5, воно буде надруковано в оригіналі.
Приклад:
задано набір чисел:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Ваш код має створити нову колекцію з таким результатом:
["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
"""
import doctest


#    Функція обробки послідовності по алгоритму FizzBuzz
def fizz_buzz(source: list) -> list:
    """
    :param source: вхідний набір чисел
    :return: результативний набір із заміненими значеннями відповідно до завдання
    >>> fizz_buzz([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
    """
    result = list()
    for item in source:
        div_by_3 = item % 3 == 0
        div_by_5 = item % 5 == 0
        div_by_both = div_by_3 and div_by_5
        if div_by_both:
            result.append("FizzBuzz")
        elif div_by_3:
            result.append("Fizz")
        elif div_by_5:
            result.append("Buzz")
        else:
            result.append(str(item))
    return result


def fizz_buzz_generator(n: int) -> list:
    """
    :param n: кількість чисел
    :return: набір чисел
    >>> fizz_buzz_generator(15)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    """
    result = list()
    for i in range(1, n + 1):
        result.append(i)
    return result


if __name__ == '__main__':
    doctest.testmod(verbose=True)
