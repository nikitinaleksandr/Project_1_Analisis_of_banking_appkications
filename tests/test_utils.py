from src.config import API_KEY_exchange, API_KEY_stocks
import pytest
from src.utils import day_time_now, max_five_transactions, exchange_rate, get_price_stocks_snp500
import json
import datetime
from unittest.mock import patch
from datetime import date
from unittest.mock import Mock
from dotenv import load_dotenv
load_dotenv('../.env')
import pandas as pd




@patch('datetime.datetime.now')
def test_test_day_time_now(mosk_time_now):
    '''Тестирование правильности работы функции'''
    mosk_time_now.return_value = datetime.datetime(2021, 1, 25, 14)
    assert day_time_now() == "Добрый день"


def test_max_five_transactions():
    # Создаем тестовый DataFrame с фиктивными данными
    data = {
        'Дата операции': ['01.09.2018', '15.09.2018', '20.09.2018', '25.09.2018', '28.09.2018', '30.09.2018'],
        'Сумма операции с округлением': [1000, 2000, 1500, 3000, 2500, 500]
    }
    test_df = pd.DataFrame(data)

    # Преобразуем даты в формат datetime
    test_df['Дата операции'] = pd.to_datetime(test_df['Дата операции'], dayfirst=True)

    # Теперь ты можешь использовать этот DataFrame для тестирования своей функции
    assert max_five_transactions(test_df['Дата операции']) == [['01.09.2018', '1000'], ['20.09.2018', '1500'],
                                                               ['15.09.2018', '2000'], ['28.09.2018','2500'],
                                                               ['25.09.2018','3000']]

def test_exchange_rate(mocker):
    # Создаем фиктивный ответ от API
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = json.dumps({"result": 75.0})

    # Используем mocker для замены requests.request на наш мок
    mocker.patch('requests.request', return_value=mock_response)

    # Вызываем тестируемую функцию
    result = exchange_rate()

    # Проверяем, что функция возвращает ожидаемый результат
    assert result == [75.0, 75.0]  # Ожидаем, что обе валюты вернут 75.0


def test_get_price_stocks_snp500(mocker):
    # Создаем фиктивный ответ от API
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = json.dumps({"result": 275.0})

    # Используем mocker для замены requests.request на наш мок
    mocker.patch('requests.get', return_value=mock_response)

    # Вызываем тестируемую функцию
    result = get_price_stocks_snp500()

    # Проверяем, что функция возвращает ожидаемый результат
    assert result == [275.0, 275.0]  # Ожидаем, что стоимость акций будет 275