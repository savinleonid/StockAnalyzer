import yfinance as yf
from pandas import DataFrame


def fetch_stock_data(ticker: str, period: str = '1mo'):
    """
    Fetches ticker data from yfinance in Dataframe format and returns it.
    :param ticker: str: ticker short name (AAPL)
    :param period: str: period of data to fetch (1mo - default)
    :return: DataFrame
    """
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data: DataFrame, window_size: int = 5):
    """
    Calculates and adds moving average data within window size given.
    :param data: DataFrame: ticker data
    :param window_size: int: window size
    :return: DataFrame: Updated data with moving average in it.
    """
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data

def calculate_and_display_average_price(data: DataFrame):
    """
    Calculates and displays average price of given data.
    :param data: DataFrame: ticker data
    :return: None
    """
    if 'Close' not in data.columns:
        raise ValueError("The DataFrame does not contain a 'Close' column.")
    average_price = data['Close'].mean()
    print(f"Средняя цена закрытия за период: {average_price:.2f}")