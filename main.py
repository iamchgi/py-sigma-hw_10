"""
Виконав: Григорій Чернолуцький
Homework_10

Package Version
------- -------
pip 24.3.1

"""
from create_logger import logger
from my_math import cubic_main, quadratic_main, fb, fbg, fibo

STREAM_COUNT = 15


def main() -> None:
    logger.info(fb(fbg(STREAM_COUNT)))
    logger.info(fibo(STREAM_COUNT))
    quadratic_main()
    cubic_main()
    pass


# --------------------------------- main module ----------------------------------------------
if __name__ == '__main__':
    logger.debug("We are going to start")
    main()
    logger.debug("We have done all correctly")
