from datetime import datetime
import tkinter as tk

from kivy.app import App
from kivy.uix.button import Button





def days_since_date(date_str):
    date_format = '%Y-%m-%d'  # Формат даты, например 'год-месяц-день'
    current_date = datetime.now().date()  # Текущая дата
    input_date = datetime.strptime(date_str, date_format).date()  # Вводимая пользователем дата

    days_passed = (current_date - input_date).days  # Определяем количество прошедших дней

    return days_passed


date_str = '2024-03-10'  # Пример вводимой даты
days_passed = days_since_date(date_str)
# print(f'С {date_str} прошло {days_passed} дней трезвости')

win = tk.Tk()
win.geometry(f"800x70+100+200")
win.title('Счётчик трезвозти')

# создания поля ввода, выравниевание вводимых символов по правому краю(justify), шрифт и размер цифр(font), ширина(width)
calc = tk.Entry(win, justify=tk.LEFT, font=('Arial', 30), width=60)
# выравнивание колонок и строк, выравнивание по краю(stick)
calc.grid(row=0, column=0, columnspan=3, stick='we')

calc.insert(0, f'С {date_str} прошло {days_passed} дней трезвости')

class CounterApp(App):
    def build(self):
        return Button(text=f'С {date_str} прошло {days_passed} дней трезвости')

CounterApp().run()


# win.mainloop()