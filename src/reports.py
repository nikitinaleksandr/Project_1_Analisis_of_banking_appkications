import os
from calendar import month
from pathlib import Path
import json
import pandas as pd
import logging
import pytest
from datetime import datetime
from datetime import timedelta
from typing import Optional
current_dir = Path(__file__).parent.parent.resolve()
dir_transactions_excel = current_dir/'data'/'operations.xlsx'
print(dir_transactions_excel)
from src.logger import setup_logging
current_dir = Path(__file__).parent.parent.resolve()
file_path_log = current_dir/'../log', 'reports.log'
logger = setup_logging('reports', file_path_log)


def save_report(filename=None):
    """Декоратор для записи отчета в файл."""
    def wrapper(func):
        def inner(*args, filename: Optional[str] = None, **kwargs):
            print("Функция inner:", inner)
            result = func(*args, **kwargs)
            print("Аргументы функции:", args, kwargs)
        # Имя файла по умолчанию
            if filename is None:
                file_name = f"report_{func.__name__}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

            # Сохранение результата в файл

            if not os.path.exists('data'):
                os.makedirs('data')
            file_path = f'data/{file_name}'
            print('file_path', file_path)

            def save_to_file(data, file_path):
                with open(file_path, 'w', encoding='utf-8') as file:
                    json.dump(data, file, ensure_ascii=False, indent=4)

        # if not os.path.exists('data'):
        #     os.makedirs('data')# проверка, что директория существует

            save_to_file(result, file_path)
            logger.info("Сохранение результата в файл data/file")
            print(save_to_file)
            print("Результат функции:", result)
            return result
        return inner
    return wrapper
        # setup_logging.info(f"Отчет сохранен в файл: {filename}")


@save_report()
def spending_by_category(transactions: pd.DataFrame,
                         category: str,
                         date: Optional[str] = None) -> pd.DataFrame:
    '''
    Функция, которая принимает на вход: датафрейм с транзакциями, название категории,
    опциональную дату. Если дата не передана, то берется текущая дата. Функция возвращает
    траты по заданной категории за последние три месяца (от переданной даты).
    '''

    df = pd.read_excel(dir_transactions_excel)
    transactions = df.to_dict('records')
    output_file = []
    for trans in transactions:
        if trans['Категория'] == category:
            output_file.append(trans)
    output_file_2 = []
    for date_operation in output_file:
        if pd.to_datetime(date, dayfirst=True) - timedelta(days=90) <= pd.to_datetime(date_operation['Дата операции'],
                         dayfirst=True) <= pd.to_datetime(date, dayfirst=True):
            output_file_2.append(date_operation)

    return output_file_2


if __name__ == '__main__':
    spending_by_category(pd.read_excel(dir_transactions_excel), 'Фастфуд', '11.11.2019')




