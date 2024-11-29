import yfinance as yf
from pandas import DataFrame


def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data

def calculate_and_display_average_price(data: DataFrame):
    if 'Close' not in data.columns:
        raise ValueError("The DataFrame does not contain a 'Close' column.")
    average_price = data['Close'].mean()
    print(f"Средняя цена закрытия за период: {average_price:.2f}")