"""
Виконав: Григорій Чернолуцький

Package Version
------- -------
pip 24.3.1

"""
import logging

logger = logging.getLogger("hw_10_logger")
logger.setLevel(logging.DEBUG)

# Створюємо обробник вивода на консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Створюємо обробник вивода у файл
file_handler = logging.FileHandler("hw_10.log", mode='a', encoding = "UTF-8")
file_handler.setLevel(logging.WARNING)

# Формат повідомлень
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Додаємо обробники до логера
logger.addHandler(console_handler)
logger.addHandler(file_handler)
