import pandas as pd
import os
from data_download import export_data_to_csv

def test_export_data_to_csv():
    """
    Test exporting stock data to a CSV file.
    """
    # Создание тестовых данных
    mock_data = pd.DataFrame({
        "Close": [100, 110, 105, 95, 115],
        "Volume": [1000, 1100, 1200, 900, 1500]
    })

    # Имя файла для теста
    test_filename = "test_stock_data.csv"

    # Вызов функции
    export_data_to_csv(mock_data, test_filename)

    # Проверка, что файл создан
    assert os.path.exists(test_filename), "CSV файл не был создан."

    # Проверка содержимого файла
    exported_data = pd.read_csv(test_filename, index_col=0)
    pd.testing.assert_frame_equal(mock_data, exported_data)

    # Удаление тестового файла
    os.remove(test_filename)
