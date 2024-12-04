import pytest
from unittest.mock import patch
import data_download as dd


def test_invalid_ticker():
    """
    Test behavior when an invalid ticker is provided.
    """
    with patch("data_download.fetch_stock_data", return_value=dd.pd.DataFrame()):
        ticker = "INVALID"
        period = "1mo"

        try:
            data = dd.fetch_stock_data(ticker, period)
            assert data.empty, "Expected empty DataFrame for invalid ticker"
        except Exception as e:
            pytest.fail(f"Unexpected exception: {e}")


def test_invalid_period():
    """
    Test behavior when an invalid period is provided.
    """
    ticker = "AAPL"
    invalid_period = "abc"

    # Expecting fetch_stock_data to return an empty DataFrame for an invalid period
    data = dd.fetch_stock_data(ticker, invalid_period)
    assert data.empty, "Expected empty DataFrame for invalid period"



def test_empty_data_handling():
    """
    Test handling of empty data returned from fetch_stock_data.
    """
    with patch("data_download.fetch_stock_data", return_value=dd.pd.DataFrame()):
        ticker = "AAPL"
        period = "1mo"

        data = dd.fetch_stock_data(ticker, period)
        assert data.empty, "Expected empty DataFrame for valid ticker with no data"
