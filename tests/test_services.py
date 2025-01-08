import pytest
from src.services import simple_search
import json

from typing import Any, Dict, List, Union
import logging
from src.logger import setup_logging
from pathlib import Path


# @pytest.mark.parametrize("search_str, transactions", [{
#             "id": 939719570,
#             "state": "EXECUTED",
#             "date": "2018-06-30T02:08:58.425572",
#             "operationAmount": {
#                 "amount": "9824.07",
#                 "currency": {
#                     "name": "USD",
#                     "code": "USD"
#                 }
#             },
#             "description": "Перевод организации",
#             "from": "Счет 75106830613657916952",
#             "to": "Счет 11776614605963066702"
#         }])



@pytest.fixture
def coll():
    return [{
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }]
# assert json.loads(simple_search(search_str="USD", transactions=coll)) == ...

def test_simple_search(coll):
    '''Тестирование правильности работы функции'''
    assert simple_search(search_str="USD", transactions=coll) == json.dumps(coll)


def test_simple_search_not_search_str(coll):
    '''Тестирование правильности работы функции при отсутствии search_str'''

    assert simple_search(search_str = "", transactions=coll) == []

def test_simple_search_not_search_str(coll):
    '''Тестирование правильности работы функции при отсутствии transactions'''

    assert simple_search(search_str = "USD", transactions="") == []


def test_simple_search_not_search_str(coll):
    '''Тестирование правильности работы функции при отсутствии search_str в transactions'''

    assert json.loads((simple_search(search_str = "fG", transactions=coll))) == []

def test_simple_search_not_str_search_str(coll):
    '''Тестирование правильности работы функции при неверном типе данных search_str'''

    with pytest.raises(TypeError, match="Неверный тип данных"):
        simple_search(search_str=11, transactions=coll)