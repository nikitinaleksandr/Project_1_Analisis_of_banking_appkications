import pytest
import pandas as pd
from unittest import mock
from src.utils import day_time_now, user_transactions, max_five_transactions, exchange_rate, get_price_stocks_snp500
from datetime import datetime

data = {
    'Дата операции': ['29.09.2018', '30.09.2018', '01.10.2018'],
    'Номер карты': ['*7197', '*4556', '*7197'],
    'Сумма операции с округлением': [186388.77, 181404.21, 150000.00]
}

df = pd.DataFrame(data)


def test_day_time_now():
    current_hour = pd.Timestamp.now().hour
    greeting = day_time_now()
    
    if 0 <= current_hour < 6 or 22 <= current_hour <= 23:
        assert greeting == "Доброй ночи"
    elif 17 <= current_hour <= 22:
        assert greeting == "Добрый вечер"
    elif 7 <= current_hour <= 11:
        assert greeting == "Доброе утро"
    else:
        assert greeting == "Добрый день"


@mock.patch('pandas.read_excel', return_value=df)
def test_user_transactions(mock_read_excel):
    result = user_transactions(pd.to_datetime('29-09-2018', dayfirst=True))
    
    # expected = pd.DataFrame({
    #     'Сумма операции с округлением': [186388.77, 181404.21],
    #     'кэшбек': [1863.0, 1814.0]
    # }, index=pd.Index(['*7197', '*4556'], name='Номер карты'))

    expected = pd.DataFrame({
        'Сумма операции с округлением': [186388.77],
        'кэшбек': [1863.0]
    }, index=pd.Index(['*7197'], name='Номер карты'))
    
    pd.testing.assert_frame_equal(result, expected)


# @mock.patch('pandas.read_excel', return_value=df)
# def test_max_five_transactions(mock_read_excel):
#     result = max_five_transactions(pd.to_datetime('30-09-2018', dayfirst=True))
#
#     filtered_df = df[df['Дата операции'] <= '30.09.2018']
#     expected = filtered_df.sort_values(by='Сумма операции с округлением', ascending=False).head(5)
#
#     pd.testing.assert_frame_equal(result, expected)


# Создаем тестовые данные
transactions_data = {
    'Дата операции': [
        '2023-10-01', '2023-10-05', '2023-10-10',
        '2023-10-15', '2023-10-20', '2023-10-25'
    ],
    'Сумма операции с округлением': [100, 200, 300, 400, 500, 600]
}

df_test = pd.DataFrame(transactions_data)


# Функция для теста

def test_max_five_transactions(monkeypatch):
    # Патчим метод read_excel, чтобы он возвращал наш тестовый DataFrame
    monkeypatch.setattr(pd, "read_excel", lambda _: df_test)

    # Дата для фильтрации
    test_date = datetime(2023, 10, 15)

    # Ожидаемый результат
    expected_result = df_test.loc[2:5].sort_values(
        by='Сумма операции с округлением', ascending=False
    ).head(5)

    # Вызов тестируемой функции
    result = max_five_transactions(test_date)

    # Проверка
    # pd.testing.assert_frame_equal(result, expected_result)
    # pd.testing.assert_frame_equal(result, expected_result, check_index=False)
    # pd.testing.assert_frame_equal(result, expected_result, check_like=True)

    result = result.reset_index(drop=True)
    expected_result = expected_result.reset_index(drop=True)
    pd.testing.assert_frame_equal(result, expected_result)










@mock.patch('requests.get')
def test_exchange_rate(mock_requests_get):
    mock_requests_get.side_effect = [
        mock.Mock(json=lambda: {
            "success": True,
            "result": 94.16688
        }),
        mock.Mock(json=lambda: {
            "success": True,
            "result": 97.275313
        })
    ]
    
    result = exchange_rate()
    expected = [94.16688, 97.275313]
    
    assert result == expected


@mock.patch('requests.get')
def test_get_price_stocks_snp500(mock_requests_get):
    stock_prices = [
        {'price': '232.62000'},
        {'price': '232.75999'},
        {'price': '185.32001'},
        {'price': '411.44000'},
        {'price': '328.5'}
    ]
    
    mock_requests_get.side_effect = [
        mock.Mock(json=lambda: stock_prices[0]),
        mock.Mock(json=lambda: stock_prices[1]),
        mock.Mock(json=lambda: stock_prices[2]),
        mock.Mock(json=lambda: stock_prices[3]),
        mock.Mock(json=lambda: stock_prices[4])
    ]
    
    result = get_price_stocks_snp500()
    expected = ['232.62000', '232.75999', '185.32001', '411.44000', '328.5']
    
    assert result == expected


if __name__ == "__main__":
    pytest.main()
