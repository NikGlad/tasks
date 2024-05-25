# Разработать приложение для определения знака зодиака по дате рождения.
# Пример:
#
# Введите месяц: март
# Введите число: 6
#
# Вывод:
# Рыбы


mounth = input("Введите месяц: ")
day =  int(input("Введите день: "))

if mounth == "март" and 21<=day<=31 or mounth == "апрель" and 1<=day<=19:
    print("Овен")

elif mounth == "апрель" and 20<=day<=30 or mounth == "май" and 1<=day<=20:
    print("Телец")

elif mounth == "май" and 21<=day<=31 or mounth == "июнь" and 1<=day<=21:
    print("Близнецы")

elif mounth == "июнь" and 22<=day<=30 or mounth == "июль" and 1<=day<=22:
    print("Рак")

elif mounth == "июль" and 23<=day<=31 or mounth == "август" and 1<=day<=22:
    print("Лев")

elif mounth == "август" and 23<=day<=31 or mounth == "сентябрь" and 1<=day<=22:
    print("Лев")

elif mounth == "сентябрь" and 23<=day<=30 or mounth == "октябрь" and 1<=day<=23:
    print("Весы")

elif mounth == "октябрь" and 24<=day<=31 or mounth == "ноябрь" and 1<=day<=21:
    print("Скорпион")

elif mounth == "ноябрь" and 22<=day<=30 or mounth == "декабрь" and 1<=day<=21:
    print("Стрелец")

elif mounth == "декабрь" and 22<=day<=31 or mounth == "январь" and 1<=day<=20:
    print("Козерог")

elif mounth == "январь" and 21<=day<=31 or mounth == "февраль" and 1<=day<=20:
    print("Водолей")

elif mounth == "февраль" and 21<=day<=29 or mounth == "март" and 1<=day<=20:
    print("Рыбы")
