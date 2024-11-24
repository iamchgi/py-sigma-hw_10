# Клас для реалізації обчислення ряду чисел Фібоначчі за допомогою ітератора
import doctest

# Клас ітератора чисел Фібоначчі
class Fibonacci:
    last = 0
    current = 1

    def __init__(self, n):
        self.index = 1
        self.max = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > self.max:
            raise StopIteration

        result = self.last
        self.last, self.current = self.current, self.last + self.current
        self.index += 1
        return result

def fibonacci_iterator(n) -> list:
    """
    :param n: Кількість чисел Фібоначчі
    :return:  Послідовність чисел Фібоначчі у кількісті n
    >>> fibonacci_iterator(15)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
    >>> fibonacci_iterator(10)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    >>> fibonacci_iterator(0)
    []
    """
    fib_iter = Fibonacci(n)
    result = []
    for i in fib_iter:
        result.append(i)
    return result

if __name__ == '__main__':
    doctest.testmod(verbose=True)