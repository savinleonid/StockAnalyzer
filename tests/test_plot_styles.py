import pytest
from matplotlib import pyplot as plt

import data_plotting as dplt
import pandas as pd
import os


def test_create_plot_with_styles():
    mock_data = pd.DataFrame({
        "Close": [100, 102, 104, 103, 105],
        "Moving_Average": [100, 101, 102, 102.5, 103]
    })
    valid_style = "seaborn-v0_8" if "seaborn-v0_8" in plt.style.available else "ggplot"
    filename = "test_plot.png"

    try:
        dplt.create_and_save_plot_with_indicators(
            data=mock_data,
            ticker="TEST",
            period="custom",
            filename=filename,
            style=valid_style
        )
        assert os.path.exists(filename), f"Файл {filename} не был создан."
    except Exception as e:
        pytest.fail(f"Plot creation with style '{valid_style}' failed: {e}")
    finally:
        # Удаление файла после выполнения теста
        if os.path.exists(filename):
            os.remove(filename)


def test_create_interactive_plot():
    mock_data = pd.DataFrame({
        "Close": [100, 102, 104, 103, 105, 107, 110],
        "Moving_Average": [100, 101, 103, 103, 104, 106, 108]
    }, index=pd.date_range(start="2023-01-01", periods=7))

    test_filename = "test_interactive_chart.html"

    try:
        # Создаём интерактивный график
        dplt.create_interactive_plot(mock_data, "TEST", filename=test_filename)

        # Проверяем, что файл создан
        assert os.path.exists(test_filename), "Файл интерактивного графика не был создан."

    except Exception as e:
        pytest.fail(f"Интерактивный график не удалось создать: {e}")

    finally:
        # Удаляем тестовый файл
        if os.path.exists(test_filename):
            os.remove(test_filename)