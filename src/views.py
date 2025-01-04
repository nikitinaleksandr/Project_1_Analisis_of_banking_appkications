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
    print(sorted_by_sale)


if __name__ == '__main__':
     user_transactions(pd.to_datetime('29.09.2018', dayfirst=True))

def max_five_transactions(data_time: pd) -> list:
    """
    Функция, которая Топ-5 транзакций по сумме платежа.
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
    # sale_by_excel_data1 = df['Номер карты']['Сумма операции с округлением']


    # sorted_by_sale=sale_by_excel_data.sort_values(by='Сумма операции с округлением', ascending=False)

    # sorted_by_sale = sorted_by_sale.append()
    # print(df.head().Номер карты)
    # columns_list = sale_by_excel_data.tolist()
    # print(columns_list)
    # print(sale_by_excel_data)
    # print(sale_by_excel_data1)

#
# ,'Сумма операции с округлением','Бонусы (включая кэшбэк)'

# def max_transactions(data_time: str) -> list:
#     """
#     Функция, которая выводит ТОП-5 транзакций по сумме платежа.
#     """
#
#     df = pd.read_excel(dir_transactions_excel)
#     df_ascending = df.sort_values(by='Сумма операции с округлением', ascending=False)
#     print(df_ascending)
#     replecement = '01'
#     res = data_time.replace(data_time[0:2], replecement, 1)
#
#
#
#
#     df1 = df.loc[((df['Дата операции'])<=data_time) & ((df['Дата операции']) >= res)]
#     sale_by_excel_data1 = df.sort_values(by='Сумма операции с округлением', ascending=False)
#     sale_by_excel_data = df1.sort_values(by='Сумма операции с округлением', ascending=False)
#     print(df1)
#     print(sale_by_excel_data)
#     print(df.head())
#     print(sale_by_excel_data1)
#     if __name__ == '__main__':
#         max_transactions('2018.01.10')