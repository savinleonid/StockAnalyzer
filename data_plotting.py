import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame


def create_and_save_plot(data: DataFrame, ticker: str, period: str, filename: str = None):
    """
    Creates and plots graph for ticker in given period and saves in PNG format.
    :param data: Dataframe
    :param ticker: str
    :param period: str
    :param filename: str
    :return: None
    """
    plt.figure(figsize=(10, 6))

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')

    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()

    # standard naming if not provided
    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")

def create_and_save_plot_with_indicators(data: DataFrame, ticker: str, period: str, filename: str = "stock_chart_with_indicators.png"):
    """
    Creates a plot with closing prices and additional indicators (RSI and MACD).
    :param data: DataFrame: Stock data.
    :param ticker: str: Ticker of the stock.
    :param period: str: Period of the stock data.
    :param filename: str: Name of the file to save the plot (default: 'stock_chart_with_indicators.png').
    :return: None
    """
    fig, axs = plt.subplots(3, figsize=(12, 10), sharex=True)

    # Plot closing price
    axs[0].plot(data['Close'], label='Closing Price', color='blue')
    axs[0].set_title(f"{ticker} Closing Price")
    axs[0].legend()

    # Plot RSI
    if 'RSI' in data.columns:
        axs[1].plot(data['RSI'], label='RSI (14)', color='green')
        axs[1].axhline(70, color='red', linestyle='--', linewidth=0.7)
        axs[1].axhline(30, color='red', linestyle='--', linewidth=0.7)
        axs[1].set_title(f"{ticker} RSI (Relative Strength Index)")
        axs[1].legend()

    # Plot MACD
    if 'MACD' in data.columns and 'Signal_Line' in data.columns:
        axs[2].plot(data['MACD'], label='MACD', color='purple')
        axs[2].plot(data['Signal_Line'], label='Signal Line', color='orange')
        axs[2].set_title(f"{ticker} MACD")
        axs[2].legend()

    plt.tight_layout()
    plt.savefig(filename)
    plt.show()
    print(f"График с индикаторами сохранён как {filename}")
