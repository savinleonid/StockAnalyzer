import data_download as dd
import data_plotting as dplt
import matplotlib.pyplot as plt


def validate_style(style):
    """
    Проверяет доступность указанного стиля графика.
    Если стиль недоступен, возвращает 'default'.
    :param style: str: стиль графика
    :return: str: корректный стиль
    """
    if style not in plt.style.available:
        print(f"Предупреждение: Стиль '{style}' недоступен. Используется стиль по умолчанию 'default'.")
        return "default"
    return style


def main():
    """
    Добро пожаловать в инструмент анализа и визуализации биржевых данных.
    Вы можете выбрать предустановленный период (например, '1mo', '6mo', '1y')
    или указать конкретные даты начала и окончания анализа.

    Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть:
    AAPL (Apple Inc),
    GOOGL (Alphabet Inc),
    MSFT (Microsoft Corporation),
    AMZN (Amazon.com Inc),
    TSLA (Tesla Inc).

    Общие периоды времени для данных о запасах включают:
    1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.
    """
    print(main.__doc__)  # Выводим документацию

    try:
        # Ввод тикера
        ticker = input("Введите тикер акции (например, 'AAPL' для Apple Inc): ").strip().upper()
        if not ticker:
            raise ValueError("Тикер не может быть пустым!")

        # Выбор периода
        period_choice = input("Хотите использовать предустановленный период? (да/нет): ").strip().lower()
        if period_choice == 'да':
            period = input("Введите период (например, '1mo', '6mo', '1y'): ").strip().lower()
            if not period:
                raise ValueError("Период не может быть пустым!")
            start_date = None
            end_date = None
        else:
            start_date = input("Введите начальную дату (в формате YYYY-MM-DD): ").strip()
            end_date = input("Введите конечную дату (в формате YYYY-MM-DD): ").strip()
            if not start_date or not end_date:
                raise ValueError("Начальная и конечная даты не могут быть пустыми!")
            period = None

        # Загрузка данных
        stock_data = dd.fetch_stock_data(ticker, period=period, start_date=start_date, end_date=end_date)
        if stock_data.empty:
            raise ValueError("Не удалось загрузить данные. Проверьте тикер и даты.")

        # Остальные шаги с обработкой ошибок
        try:
            stock_data = dd.add_moving_average(stock_data)
            stock_data = dd.calculate_rsi(stock_data)
            stock_data = dd.calculate_macd(stock_data)
        except Exception as e:
            print(f"Ошибка при расчёте индикаторов: {e}")
            return

        # Вывод средней цены
        dd.calculate_and_display_average_price(stock_data)

        # Уведомление о колебаниях
        try:
            dd.notify_if_strong_fluctuations(stock_data, threshold=5.0)
        except Exception as e:
            print(f"Ошибка при уведомлении о колебаниях: {e}")

        # Выбор стиля графика
        print("Доступные стили графиков:", ", ".join(plt.style.available))
        style = input("Введите стиль графика (например, 'seaborn-v0_8', 'ggplot' или 'default'): ").strip()
        style = validate_style(style)

        # Построение графика
        try:
            filename = f"{ticker}_custom_chart.png"
            dplt.create_and_save_plot_with_indicators(stock_data, ticker, "custom", filename, style=style)
            print(f"График сохранён как {filename}")
        except Exception as e:
            print(f"Ошибка при создании графика: {e}")

        # Экспорт данных
        try:
            export_filename = f"{ticker}_custom_data.csv"
            dd.export_data_to_csv(stock_data, export_filename)
            print(f"Данные сохранены в файл: {export_filename}")
        except Exception as e:
            print(f"Ошибка при экспорте данных: {e}")

    except ValueError as ve:
        print(f"Ошибка ввода: {ve}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")


if __name__ == "__main__":
    main()
