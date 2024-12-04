import pandas as pd
from data_download import notify_if_strong_fluctuations

def test_notify_if_strong_fluctuations_exceeds_threshold():
    """
    Test the function when price fluctuation exceeds the threshold.
    """
    # Mock data where fluctuation exceeds 10%
    mock_data = pd.DataFrame({
        "Close": [100, 150, 120, 80, 140]
    })
    threshold = 10.0

    # Capture the output
    import io
    import sys
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Call the function
    fluctuation = notify_if_strong_fluctuations(mock_data, threshold)

    # Reset stdout
    sys.stdout = sys.__stdout__

    # Verify the fluctuation and printed message
    output = captured_output.getvalue()
    assert fluctuation > threshold
    assert f"Колебания цены составили {fluctuation:.2f}%" in output

def test_notify_if_strong_fluctuations_below_threshold():
    """
    Test the function when price fluctuation is below the threshold.
    """
    # Mock data where fluctuation is less than 10%
    mock_data = pd.DataFrame({
        "Close": [100, 105, 102, 101, 104]
    })
    threshold = 10.0

    # Capture the output
    import io
    import sys
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Call the function
    fluctuation = notify_if_strong_fluctuations(mock_data, threshold)

    # Reset stdout
    sys.stdout = sys.__stdout__

    # Verify the fluctuation and printed message
    output = captured_output.getvalue()
    assert fluctuation < threshold
    assert f"Колебания цены составили {fluctuation:.2f}%" in output

def test_missing_close_column_task2():
    """
    Test the function with missing 'Close' column.
    """
    # Mock data without 'Close' column
    mock_data = pd.DataFrame({
        "Open": [100, 150, 120, 80, 140]
    })
    threshold = 10.0

    # Verify that the function raises a ValueError
    try:
        notify_if_strong_fluctuations(mock_data, threshold)
    except ValueError as e:
        assert str(e) == "The DataFrame does not contain a 'Close' column."
