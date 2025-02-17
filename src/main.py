import datetime
from datetime import datetime
import typing
import json
import pandas as pd
from typing import Any, Dict, List, Union
# from views import website
from utils import day_time_now, user_transactions, max_five_transactions, exchange_rate, get_price_stocks_snp500
from src.services import transactions
from src.views import website
from services import simple_search
def main() -> Any:
    """Функция для запуска всего проекта"""
# Главная страница
print("\nГЛАВНАЯ\n")
# print(website('29-09-2018 00:00:00'))
# print("Функция website запущена")
# Страница Событие
print("\nСОБЫТИЕ\n")
seach_str= input('Введите строку поиска: ')
simple_search(seach_str, transactions)


# Страница Отчеты
print("\nОТЧЕТЫ\n")

# if __name__ == '__main__':
#     print("\nГЛАВНАЯ\n")
#     print(website('29-09-2019 00:00:00'))
# if __name__ == '__main__':
#     data_time = "29-09-2018 00:00:00" # или другая дата
#     result = website(data_time)
#     print(result)
    # data_time = pd.Timestamp("29-09-2018 00:00:00")  # Пример даты
    # result = user_transactions(data_time)
    # print("Результат транзакций:")
    # print(result)

# if __name__ == '__main__':
#     data_time = "29-09-2018 00:00:00"  # или другая дата
#     print(f"Перед вызовом website: {data_time}")
#     result = website(data_time)
#     print(f"Результат: {result}")
#     main()
# if __name__ == '__main__':
#     data_time = pd.Timestamp("29-09-2018 00:00:00")
#     result1, result2, result3, result4, result5 = website(data_time)
#     print(result1, result2, result3, result4, result5)


# if __name__ == '__main__':
#
#     print(f'{day_time_now()}')
#     # print(user_transactions(pd.to_datetime('29-09-2018 00:00:00', dayfirst=True)))
#     data_time = pd.Timestamp("29-09-2018 00:00:00")  # Пример даты
#     result = user_transactions(data_time)
#     print("Результат транзакций:")
#     print(result)
#     print("Пять максимальных транзакций:")
#     print(max_five_transactions(data_time))
#     print("Курсы валют:")
#     print(exchange_rate())
#     print("stocks_snp500:")
#     print(get_price_stocks_snp500())

if __name__ == '__main__':
    print("Перед вызовом website")
    data_time = pd.Timestamp("29-09-2018 00:00:00")
    result1, result2, result3, result4, result5 = website(data_time)
    print("После вызова website")
    print(result1, result2, result3, result4, result5)