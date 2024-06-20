from datetime import datetime


def days_since_date(date_str):
    date_format = '%Y-%m-%d'  # Формат даты, например 'год-месяц-день'
    current_date = datetime.now().date()  # Текущая дата
    input_date = datetime.strptime(date_str, date_format).date()  # Вводимая пользователем дата

    days_passed = (current_date - input_date).days  # Определяем количество прошедших дней

    return days_passed


date_str = '2024-03-10'  # Пример вводимой даты
days_passed = days_since_date(date_str)
print(f'С {date_str} прошло {days_passed} дней')