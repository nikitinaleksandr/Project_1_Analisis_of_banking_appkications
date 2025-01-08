import datetime
import typing
import json
from typing import Any, Dict, List, Union
# from views import website
from utils import day_time_now, user_transactions, max_five_transactions, exchange_rate, get_price_stocks_snp500
from src.services import transactions
from services import simple_search
def main() -> Any:
    """Функция для запуска всего проекта"""
# Главная страница
print("\nГЛАВНАЯ\n")
# print(website(data_time, ))

# Страница Событие
print("\nСОБЫТИЕ\n")
seach_str= input('Введите строку поиска: ')
simple_search(seach_str, transactions)


# Страница Отчеты
print("\nОТЧЕТЫ\n")



if __name__ == '__main__':
    main()