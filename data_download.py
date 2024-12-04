import yfinance as yf
from pandas import DataFrame
import pandas as pd


def fetch_stock_data(ticker: str, period: str = '1mo') -> DataFrame:
    """
    Fetches ticker data from yfinance in DataFrame format and returns it.
    :param ticker: str: Ticker short name (e.g., 'AAPL').
    :param period: str: Period of data to fetch (e.g., '1mo' for one month).
    :return: DataFrame: Historical stock data.
    """
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data: DataFrame, window_size: int = 5) -> DataFrame:
    """
    Calculates and adds moving average data within the given window size.
    :param data: DataFrame: Historical stock data.
    :param window_size: int: Size of the moving average window (default is 5).
    :return: DataFrame: Updated DataFrame with moving average column.
    """
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data: DataFrame):
    """
    Calculates and displays the average closing price for the given data.
    :param data: DataFrame: Historical stock data.
    :return: None
    """
    if 'Close' not in data.columns:
        raise ValueError("The DataFrame does not contain a 'Close' column.")
    average_price = data['Close'].mean()
    print(f"Средняя цена закрытия за период: {average_price:.2f}")


def notify_if_strong_fluctuations(data: DataFrame, threshold: float) -> float:
    """
    Analyzes price fluctuations and notifies the user if they exceed a threshold.
    :param data: DataFrame: Historical stock data.
    :param threshold: float: Threshold percentage for price fluctuations.
    :return: float: Actual percentage fluctuation.
    """
    if 'Close' not in data.columns:
        raise ValueError("The DataFrame does not contain a 'Close' column.")

    # Calculate maximum and minimum close prices
    max_close = data['Close'].max()
    min_close = data['Close'].min()

    # Calculate percentage fluctuation
    fluctuation = ((max_close - min_close) / min_close) * 100

    # Notify the user if fluctuation exceeds the threshold
    if fluctuation > threshold:
        print(f"Внимание! Колебания цены составили {fluctuation:.2f}%, что превышает порог {threshold}%.")
    else:
        print(f"Колебания цены составили {fluctuation:.2f}%, что ниже порога {threshold}%.")

    return fluctuation
