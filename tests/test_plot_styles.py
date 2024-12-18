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
