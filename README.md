# Инструмент анализа и визуализации данных акций

Этот проект предоставляет инструмент для анализа и визуализации данных об акциях. Он загружает исторические данные с помощью библиотеки `yfinance`, вычисляет скользящие средние, уведомляет о сильных колебаниях цен и создаёт графики. Пользователи могут вводить тикеры акций и периоды для анализа.

---

## Основные функции

- Загрузка исторических данных об акциях с использованием `yfinance`.
- Вычисление и отображение средней цены закрытия.
- Уведомление о сильных колебаниях цен.
- Создание и сохранение графиков с ценами закрытия и скользящими средними.
- Обработка некорректных данных, включая:
  - Неверные тикеры акций.
  - Неподдерживаемые периоды времени.
- Полное тестирование с использованием `pytest`.

---

## Установка

### Требования

- Python 3.9 или новее.
- Виртуальная среда (рекомендуется).

### Шаги

1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/savinleonid/StockAnalyzer.git
   cd StockAnalyzer
   ```
2. Создайте и активируйте виртуальную среду:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # На Windows: .venv\Scripts\activate
   ```
3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```
   
---

## Использование
### 1. Запустите главный скрипт:
```bash
python main.py
```
### 2. Следуйте инструкциям:
- Введите тикер акции (например, AAPL для Apple Inc.).
- Введите период времени (например, 1mo для одного месяца).

### 3. Получите результаты:
- Средняя цена закрытия.
- Уведомления о сильных колебаниях цен.
- Созданный и сохранённый график.

---

## Тестирование
Для тестирования используется pytest. Чтобы запустить тесты, выполните:
```bash
pytest tests/
```

---

## Структура проекта
```bash
project/
├── data_download.py          # Модуль для загрузки и обработки данных об акциях
├── data_plotting.py          # Модуль для построения графиков
├── main.py                   # Главный скрипт для взаимодействия с пользователем
├── tests/                    # Папка с тестами
│   ├── test_calculate_average_price.py
│   ├── test_task2.py
│   ├── test_main_error_handling.py
│   └── __init__.py
├── requirements.txt          # Список зависимостей
└── README.md                 # Документация проекта
```
