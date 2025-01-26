from config import API_KEY_exchange, API_KEY_stocks
import datetime
import requests
import json
import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv('../.env')
import logging
from src.logger import setup_logging
from pathlib import Path

import pandas as pd
current_dir = Path(__file__).parent.parent.resolve()

dir_transactions_excel = current_dir/'data'/'operations.xlsx'
print(dir_transactions_excel)


def day_time_now():
    """
    Функция - приветствие в формате — «Доброе утро» / «Добрый день» / «Добрый вечер» / «Доброй ночи» в зависимости
    от текущего времени.
    """
    current_date_time = datetime.datetime.now()
    hour = current_date_time.hour
    if 0 <= hour < 6 or 22 <= hour <= 23:
        return "Доброй ночи"
    elif 17 <= hour <= 22:
        return "Добрый вечер"
    elif 7 <= hour <= 11:
        return "Доброе утро"
    else:
        return "Добрый день"
# print(hour)
# print(current_date_time)

if __name__ == '__main__':
    day_time_now()


def user_transactions(data_time: pd) -> list:
    """
    Функция, которая выводит по каждой карте:
    последние 4 цифры карты;
    общая сумма расходов;
    кешбэк (1 рубль на каждые 100 рублей).
    """

    df = pd.read_excel(dir_transactions_excel)
    df1 = df.loc[((pd.to_datetime(df['Дата операции'], dayfirst=True)) <= data_time) &
                 ((pd.to_datetime(df['Дата операции'], dayfirst=True)) >= data_time.replace(day=1))]
    filtered_df1 = df1.copy()
    filtered_df1.loc[:, 'кэшбек'] = filtered_df1['Сумма операции с округлением'] // 100
    sale_by_excel_data = filtered_df1.groupby('Номер карты')[['Сумма операции с округлением', 'кэшбек']].sum()
    sorted_by_sale = sale_by_excel_data.sort_values(by='Сумма операции с округлением', ascending=False)
    type(sorted_by_sale)
    print(sorted_by_sale)
    return sorted_by_sale


if __name__ == '__main__':
     user_transactions(pd.to_datetime('29-09-2018 00:00:00', dayfirst=True))

def max_five_transactions(data_time: pd) -> list:
    """
    Функция, которая выводит Топ-5 транзакций по сумме платежа.
    """

    df = pd.read_excel(dir_transactions_excel)
    df1 = df.loc[((pd.to_datetime(df['Дата операции'], dayfirst=True)) <= data_time) &
                 ((pd.to_datetime(df['Дата операции'], dayfirst=True)) >= data_time.replace(day=1))]
    sorted_by_sale = df1.sort_values(by='Сумма операции с округлением', ascending=False).head(5)
    print(sorted_by_sale)


if __name__ == '__main__':
     max_five_transactions(pd.to_datetime('29.09.2018', dayfirst=True))


    # print(df.shape)
    # print(df.head())


def exchange_rate():
    """
    Функция, которая выводит курс валют в USD и EUR к RUB, происходит обращение к внешнему API
    """
    # API_KEY_exchange = os.getenv('API_KEY_exchange')
    currency_list = ["USD", "EUR"]
    convert_to = "RUB"
    amount = 1
    new_currency_list = []
    for currency in currency_list:

        url = f"https://api.apilayer.com/currency_data/convert?to={convert_to}&from={currency}&amount={amount}"

        payload = {}
        headers = {
            "apikey": API_KEY_exchange
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        # response = requests.get(url) #Получение данных с сервера
        result = response.text # Получение текстовой части данных
        parst_result = json.loads(result)
        returned_result = parst_result
        new_currency_list.append(returned_result['result'])
        # return returned_result['result']
        # print(returned_result)
    return new_currency_list
if __name__ == '__main__':
    print(exchange_rate())


def get_price_stocks_snp500():
    """
    Функция, которая выводит стоимость акций из списка snp500, происходит обращение к внешнему API
    """
    stocks_list = ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]
    price_stocks_in_stocks_list = []
    # API_KEY_stocks = os.getenv('API_KEY_stocks')
    for stock in stocks_list:
        response = requests.get(f"https://api.twelvedata.com/price?symbol={stock}&apikey={API_KEY_stocks}")
        json_str = response.text
        dict_result = json.loads(json_str)
        price_element = dict_result.get('price')
        price_stocks_in_stocks_list.append(price_element)
    return price_stocks_in_stocks_list
if __name__ == '__main__':
    print(get_price_stocks_snp500())