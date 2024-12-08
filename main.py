import data_download as dd
import data_plotting as dplt


def main():
    """
    Добро пожаловать в инструмент получения и построения графиков биржевых данных.

    Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть:
    AAPL (Apple Inc),
    GOOGL (Alphabet Inc),
    MSFT (Microsoft Corporation),
    AMZN (Amazon.com Inc),
    TSLA (Tesla Inc).

    Общие периоды времени для данных о запасах включают:
    1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.
    """
    print(main.__doc__)  # print documentation

    # Получение данных от пользователя
    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc): ").strip().upper()
    period = input("Введите период для данных (например, '1mo' для одного месяца): ").strip().lower()

    try:
        # Загрузка данных акций
        stock_data = dd.fetch_stock_data(ticker, period)

        # Проверка, что данные не пусты
        if stock_data.empty:
            print(f"Данные для тикера '{ticker}' за период '{period}' не найдены. Проверьте ввод.")
            return
    except Exception as e:
        print(f"Ошибка загрузки данных: {e}")
        return

    try:
        # Добавление скользящего среднего
        stock_data = dd.add_moving_average(stock_data)

        # Вывод средней цены
        dd.calculate_and_display_average_price(stock_data)

        # Уведомление о сильных колебаниях
        dd.notify_if_strong_fluctuations(stock_data, 5.0)

        # Построение графика и сохранение
        filename = f"{ticker}_{period}_stock_chart.png"
        dplt.create_and_save_plot(stock_data, ticker, period, filename)

        # Экспорт данных в CSV
        csv_filename = f"{ticker}_{period}_data.csv"
        dd.export_data_to_csv(stock_data, csv_filename)
    except Exception as e:
        print(f"Ошибка обработки данных: {e}")
        return


if __name__ == "__main__":
    main()
