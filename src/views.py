import datetime
import requests
import json
import os
from pathlib import Path
from dotenv import load_dotenv
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
    print("Доброй ночи")
elif 17 <= hour <= 22:
    print("Добрый вечер")
elif 7 <= hour <= 11:
    print("Доброе утро")
else:
    print("Добрый день")
# print(hour)
# print(current_date_time)

if __name__ == '__main__':
    day_time_now()


def user_transactions(data_time: str) -> list:
    """
    Функция, которая выводит по каждой карте:
    последние 4 цифры карты;
    общая сумма расходов;
    кешбэк (1 рубль на каждые 100 рублей).
    """

    df = pd.read_excel(dir_transactions_excel)
    replecement = '01'
    res = data_time.replace(data_time[0:2], replecement, 1)



    # Использование метода replace для замены даты

    # print(res)
    # df1 = df.loc[(df['Дата операции'])>=res & (df['Дата операции'])<=data_time]
    df1 = df.loc[((df['Дата операции'])<=data_time) & ((df['Дата операции']) >= res)]
    # print(df.shape)
    # print(df.head())
    # sale_by_excel_data1 = df['Номер карты']['Сумма операции с округлением']
    sale_by_excel_data = df1.groupby('Номер карты', )['Сумма операции с округлением'].sum()

    # sorted_by_sale=sale_by_excel_data.sort_values(by='Сумма операции с округлением', ascending=False)
    sorted_by_sale = sale_by_excel_data.sort_values(ascending=False)
    # sorted_by_sale = sorted_by_sale.append()
    # print(df.head().Номер карты)
    # columns_list = sale_by_excel_data.tolist()
    # print(columns_list)
    # print(sale_by_excel_data)
    # print(sale_by_excel_data1)
    print(sorted_by_sale)
# user_transactions('2018.01.10')
#
# ,'Сумма операции с округлением','Бонусы (включая кэшбэк)'

def max_transactions(data_time: str) -> list:
    """
    Функция, которая выводит ТОП-5 транзакций по сумме платежа.
    """

    df = pd.read_excel(dir_transactions_excel)
    df_ascending = df.sort_values(by='Сумма операции с округлением', ascending=False)
    print(df_ascending)
    replecement = '01'
    res = data_time.replace(data_time[0:2], replecement, 1)




    df1 = df.loc[((df['Дата операции'])<=data_time) & ((df['Дата операции']) >= res)]
    sale_by_excel_data1 = df.sort_values(by='Сумма операции с округлением', ascending=False)
    sale_by_excel_data = df1.sort_values(by='Сумма операции с округлением', ascending=False)
    print(df1)
    print(sale_by_excel_data)
    print(df.head())
    print(sale_by_excel_data1)
    if __name__ == '__main__':
        max_transactions('2018.01.10')