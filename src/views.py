# from utils import day_time_now, user_transactions
import datetime
import requests
import json
import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv('../.env')
from typing import Union
from src.utils import day_time_now, user_transactions, exchange_rate, max_five_transactions, get_price_stocks_snp500

import pandas as pd
current_dir = Path(__file__).parent.parent.resolve()

dir_transactions_excel = current_dir/'data'/'operations.xlsx'
print(dir_transactions_excel)


def website(data_time: datetime) -> Union[list, dict]:
    """
    Главная функция, принимающую на вход строку с датой и временем в формате
    YYYY-MM-DD HH:MM:SS и возвращающую JSON-ответ со следующими данными:

    Приветствие в формате "???", где ??? — «Доброе утро» / «Добрый день» / «Добрый вечер» / «Доброй ночи» в зависимости
    от текущего времени.

    По каждой карте:
    последние 4 цифры карты;
    общая сумма расходов;
    кешбэк (1 рубль на каждые 100 рублей).

    Топ-5 транзакций по сумме платежа.

    Курс валют.

    Стоимость акций из S&P500.
    """
    print(f'{day_time_now()}')
    print(f'{user_transactions(data_time)}')
# data = {
#   "greeting": day_time_now(),
#   "cards": user_transactions(data_time),
#   "top_transactions": [
#     {
#       "date": "21.12.2021",
#       "amount": 1198.23,
#       "category": "Переводы",
#       "description": "Перевод Кредитная карта. ТП 10.2 RUR"
#     },
#     {
#       "date": "20.12.2021",
#       "amount": 829.00,
#       "category": "Супермаркеты",
#       "description": "Лента"
#     },
#     {
#       "date": "20.12.2021",
#       "amount": 421.00,
#       "category": "Различные товары",
#       "description": "Ozon.ru"
#     },
#     {
#       "date": "16.12.2021",
#       "amount": -14216.42,
#       "category": "ЖКХ",
#       "description": "ЖКУ Квартира"
#     },
#     {
#       "date": "16.12.2021",
#       "amount": 453.00,
#       "category": "Бонусы",
#       "description": "Кешбэк за обычные покупки"
#     }
#   ],
#   "currency_rates": [
#     {
#       "currency": "USD",
#       "rate": 73.21
#     },
#     {
#       "currency": "EUR",
#       "rate": 87.08
#     }
#   ],
#   "stock_prices": [
#     {
#       "stock": "AAPL",
#       "price": 150.12
#     },
#     {
#       "stock": "AMZN",
#       "price": 3173.18
#     },
#     {
#       "stock": "GOOGL",
#       "price": 2742.39
#     },
#     {
#       "stock": "MSFT",
#       "price": 296.71
#     },
#     {
#       "stock": "TSLA",
#       "price": 1007.08
#     }
#   ]
# }
# json_response = json.dumps(data, ensure_ascii=False)
# print(json_response)




if __name__ == '__main__':
    print(website('29-09-2018 00:00:00'))


