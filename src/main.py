import datetime
from datetime import datetime
import typing
import json
import pandas as pd
from typing import Any, Dict, List, Union
from src.utils import day_time_now, user_transactions, max_five_transactions, exchange_rate, get_price_stocks_snp500
from src.services import transactions
from src.views import website
from src.services import simple_search
from src.reports import spending_by_category, dir_transactions_excel


def main() -> Any:
        """Функция для запуска всего проекта"""


if __name__ == '__main__':
    print("\nГЛАВНАЯ\n")

    data_time = pd.Timestamp("29-09-2018 00:00:00")
    result1, result2, result3, result4, result5 = website(data_time)
    # print("После вызова website")
    print(result1, result2, result3, result4, result5)

    print("\nСервисы.Простой поиск\n")
    search_str = input('Введите строку поиска: ')
    simple_search(search_str, transactions)

    print("\nОТЧЕТЫ\n")
    spending_by_category(pd.read_excel(dir_transactions_excel), 'Фастфуд', '11.11.2019')
