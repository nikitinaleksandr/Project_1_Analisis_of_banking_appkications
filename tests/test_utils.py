from src.config import API_KEY_exchange, API_KEY_stocks
import pytest
from src.utils import day_time_now
import json
import datetime
from unittest.mock import patch
from datetime import date
from unittest.mock import Mock
from dotenv import load_dotenv
load_dotenv('../.env')




@patch('datetime.datetime.now')
def test_day_time_now(mosk_time_now):
    '''Тестирование правильности работы функции'''
    mosk_time_now.return_value = datetime.datetime(2021, 1, 25, 14)
    assert day_time_now() == "Добрый день"

