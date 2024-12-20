import yfinance as yf
from pandas import DataFrame
import pandas as pd


def calculate_rsi(data: DataFrame, window: int = 14) -> DataFrame:
    """
    Calculates the Relative Strength Index (RSI).
    :param data: DataFrame: Stock data.
    :param window: int: Lookback period for RSI (default is 14).
    :return: DataFrame: Updated data with RSI column.
    """
    if len(data) < window:
        raise ValueError(f"Недостаточно данных для расчёта RSI: требуется минимум {window} записей.")

    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()

    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))
    data['RSI'] = data['RSI'].fillna(0)  # Заполняем NaN значениями по умолчанию (например, 0)
    return data


def calculate_macd(data: DataFrame, short_window: int = 12, long_window: int = 26, signal_window: int = 9) -> DataFrame:
    """
    Calculates the MACD and Signal Line.
    :param data: DataFrame: Stock data.
    :param short_window: int: Short-term EMA period (default is 12).
    :param long_window: int: Long-term EMA period (default is 26).
    :param signal_window: int: Signal line EMA period (default is 9).
    :return: DataFrame: Updated data with MACD and Signal Line columns.
    """
    data['EMA12'] = data['Close'].ewm(span=short_window, adjust=False).mean()
    data['EMA26'] = data['Close'].ewm(span=long_window, adjust=False).mean()
    data['MACD'] = data['EMA12'] - data['EMA26']
    data['Signal_Line'] = data['MACD'].ewm(span=signal_window, adjust=False).mean()
    return data


def export_data_to_csv(data: DataFrame, filename: str = "stock_data.csv"):
    """
    Exports the given DataFrame to a CSV file.

    :param data: DataFrame: The stock data to export.
    :param filename: str: Name of the CSV file to save data (default: 'stock_data.csv').
    :return: None
    """
    try:
        # Сохранение данных в CSV
        data.to_csv(filename, index=True)
        print(f"Данные успешно экспортированы в файл: {filename}")
    except Exception as e:
        print(f"Ошибка при экспорте данных: {e}")


def fetch_stock_data(ticker: str, period: str = None, start_date: str = None, end_date: str = None):
    """
    Fetches ticker data from yfinance in DataFrame format and returns it.
    :param ticker: str: ticker short name (e.g., 'AAPL').
    :param period: str: pre-set period of data to fetch (e.g., '1mo', default is None).
    :param start_date: str: start date for data fetch in 'YYYY-MM-DD' format (default is None).
    :param end_date: str: end date for data fetch in 'YYYY-MM-DD' format (default is None).
    :return: DataFrame
    """
    try:
        stock = yf.Ticker(ticker)
        if period:
            data = stock.history(period=period)
        elif start_date and end_date:
            data = stock.history(start=start_date, end=end_date)
        else:
            raise ValueError("Either 'period' or both 'start_date' and 'end_date' must be provided.")
        return data
    except Exception as e:
        print(f"Ошибка загрузки данных: {e}")
        return pd.DataFrame()


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


def calculate_standard_deviation(data: pd.DataFrame):
    """
    Рассчитывает стандартное отклонение цены закрытия акций.
    :param data: DataFrame: Данные с биржи.
    :return: float: Стандартное отклонение.
    """
    if 'Close' not in data.columns:
        raise ValueError("The DataFrame does not contain a 'Close' column.")

    std_dev = data['Close'].std()
    return std_dev
