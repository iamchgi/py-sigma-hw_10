"""
Виконав: Григорій Чернолуцький
Homework_10

Package Version
------- -------
pip 24.3.1

"""
from logger_create import create_logger
from mymath import fibonacci_iterator_show

logger = create_logger()

def main() -> None:
    fb()
    fibo()
    cubic_main()
    quadratic_main()
    pass


# --------------------------------- main module ----------------------------------------------
if __name__ == '__main__':
    logger.debug("We are going to start")
    main()
    logger.critical("We are done")

