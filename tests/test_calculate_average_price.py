import pandas as pd
from data_download import calculate_and_display_average_price

def test_calculate_and_display_average_price():
    # Mock dataset with Close prices
    mock_data = pd.DataFrame({
        "Close": [100, 110, 105, 95, 115]
    })
    expected_average = sum(mock_data["Close"]) / len(mock_data["Close"])

    # Capture the output using a context manager
    import io
    import sys
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Call the function and verify the printed output
    calculate_and_display_average_price(mock_data)

    # Reset stdout
    sys.stdout = sys.__stdout__

    # Check if the printed output matches the expected average
    output = captured_output.getvalue()
    assert f"Средняя цена закрытия за период: {expected_average:.2f}" in output

def test_missing_close_column():
    # Mock dataset without Close column
    mock_data = pd.DataFrame({
        "Open": [100, 110, 105, 95, 115]
    })

    # Verify that the function raises a ValueError
    try:
        calculate_and_display_average_price(mock_data)
    except ValueError as e:
        assert str(e) == "The DataFrame does not contain a 'Close' column."
