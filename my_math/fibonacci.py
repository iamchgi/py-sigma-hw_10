# Клас для реалізації обчислення ряду чисел Фібоначчі за допомогою ітератора

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

def fibonacci_iterator_show(n) -> list:
    """

    :param n:
    :return:
    """
    fib_iter = Fibonacci(n)
    result = []
    for i in fib_iter:
        result.append(i)
        print(i, end=" ")
    print("")
    return result