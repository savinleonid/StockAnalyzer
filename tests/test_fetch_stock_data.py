from data_download import fetch_stock_data

def test_fetch_with_period():
    data = fetch_stock_data(ticker="AAPL", period="1mo")
    assert not data.empty, "Данные не загружены при использовании периода."

def test_fetch_with_dates():
    data = fetch_stock_data(ticker="AAPL", start_date="2023-01-01", end_date="2023-02-01")
    assert not data.empty, "Данные не загружены при указании дат."

def test_fetch_invalid_dates():
    data = fetch_stock_data(ticker="AAPL", start_date="2023-02-01", end_date="2023-01-01")
    assert data.empty, "Данные должны быть пустыми при некорректных датах."
