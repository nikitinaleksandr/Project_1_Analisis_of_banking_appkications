import pytest
from src.reports import spending_by_category, save_report
import json
import os
import pathlib
from pathlib import Path
# current_dir = Path(__file__).parent.parent.resolve()
# file_path_log = current_dir/'../log', 'reports.log'
import pandas as pd
base_dir = "tests"
sub_dir = "data"
file_name = "test_file.txt"
full_path = os.path.join(base_dir, sub_dir, file_name)
print(full_path)


# @pytest.fixture
# def coll_1():
#     return [
#     {
#         "Дата операции": "10.11.2020 10:23:23",
#         "Дата платежа": "11.11.2020",
#         "Номер карты": "*7197",
#         "Статус": "OK",
#         "Сумма операции": -56.0,
#         "Валюта операции": "RUB",
#         "Сумма платежа": -56.0,
#         "Валюта платежа": "RUB",
#         "Кэшбэк": float('nan'),
#         "Категория": "Фастфуд",
#         "MCC": 5814.0,
#         "Описание": "Rumyanyj Khleb",
#         "Бонусы (включая кэшбэк)": 1,
#         "Округление на инвесткопилку": 0,
#         "Сумма операции с округлением": 56.0
#     }]


def test_save_report():
    """Декоратор для записи отчета в файл. ПОКА не знаю"""
    @save_report
    def spending_by_category(transactions: pd.DataFrame,
                             category: str,
                             date: Optional[str] = None):
        pass
def test_spending_by_category(tmpdir):
    temp_file = tmpdir.join("test_file.txt")
    decorated_function = save_report(spending_by_category)
    decorated_function("some_argument")
    assert os.path.exists(temp_file)
# def test_spending_by_category(coll_1=[
#     {
#         "Дата операции": "10.11.2020 10:23:23",
#         "Дата платежа": "11.11.2020",
#         "Номер карты": "*7197",
#         "Статус": "OK",
#         "Сумма операции": -56.0,
#         "Валюта операции": "RUB",
#         "Сумма платежа": -56.0,
#         "Валюта платежа": "RUB",
#         "Кэшбэк": float('nan'),
#         "Категория": "Фастфуд",
#         "MCC": 5814.0,
#         "Описание": "Rumyanyj Khleb",
#         "Бонусы (включая кэшбэк)": 1,
#         "Округление на инвесткопилку": 0,
#         "Сумма операции с округлением": 56.0
#     }]):
#     '''Тестирование правильности работы функции'''
#
#     assert spending_by_category(coll_1, category="Фастфуд", date = '11.11.2020') == [
#     {
#         "Дата операции": "10.11.2020 10:23:23",
#         "Дата платежа": "11.11.2020",
#         "Номер карты": "*7197",
#         "Статус": "OK",
#         "Сумма операции": -56.0,
#         "Валюта операции": "RUB",
#         "Сумма платежа": -56.0,
#         "Валюта платежа": "RUB",
#         "Кэшбэк": float('nan'),
#         "Категория": "Фастфуд",
#         "MCC": 5814.0,
#         "Описание": "Rumyanyj Khleb",
#         "Бонусы (включая кэшбэк)": 1,
#         "Округление на инвесткопилку": 0,
#         "Сумма операции с округлением": 56.0
#     }]