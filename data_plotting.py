import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
import plotly.graph_objects as go


def create_and_save_plot_with_indicators(
        data: DataFrame, ticker: str, period: str,
        filename: str = "stock_chart_with_indicators.png",
        style: str = "default"
):
    """
    Creates a plot with closing prices, moving average, and additional indicators (RSI and MACD),
    including standard deviation bands around the moving average.
    :param data: DataFrame: Stock data.
    :param ticker: str: Ticker of the stock.
    :param period: str: Period of the stock data.
    :param filename: str: Name of the file to save the plot (default: 'stock_chart_with_indicators.png').
    :param style: str: Matplotlib style to use for the plot (default: 'default').
    :return: None
    """
    # Применяем стиль графика
    plt.style.use(style)

    fig, axs = plt.subplots(3, figsize=(12, 10), sharex=True)

    # Plot closing price and Moving Average
    axs[0].plot(data['Close'], label='Closing Price', color='blue')
    if 'Moving_Average' in data.columns:
        axs[0].plot(data['Moving_Average'], label='Moving Average', color='orange', linestyle='--')

        # Добавляем полосы стандартного отклонения вокруг скользящего среднего
        std_dev = data['Close'].std()
        axs[0].fill_between(
            data.index,
            data['Moving_Average'] - std_dev,
            data['Moving_Average'] + std_dev,
            color='gray', alpha=0.2, label='Standard Deviation Bands'
        )

    axs[0].set_title(f"{ticker} Closing Price, Moving Average, and Standard Deviation Bands")
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

def create_interactive_plot(data, ticker, filename="interactive_chart.html"):
    """
    Создаёт интерактивный график с использованием Plotly.
    :param data: DataFrame: Данные с индикаторами.
    :param ticker: str: Название тикера.
    :param filename: str: Имя файла для сохранения графика (по умолчанию: 'interactive_chart.html').
    :return: None
    """
    fig = go.Figure()

    # Добавление цен закрытия
    fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Closing Price'))

    # Добавление скользящего среднего
    if 'Moving_Average' in data.columns:
        fig.add_trace(go.Scatter(x=data.index, y=data['Moving_Average'], mode='lines', name='Moving Average'))

    # Настройка графика
    fig.update_layout(
        title=f"{ticker} Interactive Chart",
        xaxis_title="Date",
        yaxis_title="Price",
        template="plotly_dark"
    )

    # Сохранение графика
    fig.write_html(filename)
    print(f"Интерактивный график сохранён как {filename}")
