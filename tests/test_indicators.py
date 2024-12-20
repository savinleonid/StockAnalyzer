import math

import pandas as pd
from data_download import calculate_rsi, calculate_macd
from data_download import calculate_standard_deviation


def test_calculate_rsi():
    mock_data = pd.DataFrame({"Close": [100, 105, 102, 98, 110, 115, 108, 112, 117, 120]})
    result = calculate_rsi(mock_data, window=5)  # Уменьшено окно для теста
    assert 'RSI' in result.columns, "RSI column not added to the data."
    assert not result['RSI'].isnull().all(), "RSI calculation failed."


def test_calculate_macd():
    mock_data = pd.DataFrame({"Close": [100, 105, 102, 98, 110, 115, 108, 112, 117, 120]})
    result = calculate_macd(mock_data)
    assert 'MACD' in result.columns, "MACD column not added to the data."
    assert 'Signal_Line' in result.columns, "Signal_Line column not added to the data."
    assert not result['MACD'].isnull().all(), "MACD calculation failed."
    assert not result['Signal_Line'].isnull().all(), "Signal Line calculation failed."


def test_calculate_standard_deviation():
    mock_data = pd.DataFrame({
        "Close": [100, 102, 104, 103, 105, 107, 110]
    })
    result = calculate_standard_deviation(mock_data)
    assert result > 0, "Стандартное отклонение должно быть положительным числом."
    assert math.isclose(result, 3.31, rel_tol=1e-2), f"Неверное значение стандартного отклонения: {result}"
