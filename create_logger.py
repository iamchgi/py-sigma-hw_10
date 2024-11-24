"""
Виконав: Григорій Чернолуцький

Package Version
------- -------
pip 24.3.1

"""
import json
import logging
import logging.config

# Загрузка конфигурации из JSON-файла
with open("logging.json", "r") as f:
    config = json.load(f)
    logging.config.dictConfig(config)
# Получение логгера
logger = logging.getLogger("hw10JsonLogger")
