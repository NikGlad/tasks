# Нужно разработать приложение для финансового планирования.
# Приложение учитывает, какой процент от заработной платы уходит на ипотеку и ежемесячные расходы.
#
# Для этого пользователю предлагается ввести следующие данные:
#
# Заработную плату в месяц.
# Какой процент(%) от зп уходит на ипотеку.
# Какой процент(%) от зп уходит "на жизнь".
# Программа подсчитывает и выводит, сколько денег тратит пользователь на ипотеку и сколько он накопит за год (остаток от заработанной платы).

salary_M = float(input("Введите зарплату в месяц(руб): "))

mortgage_M = float(input("Введите, какой процент(%) уходит на ипотеку: "))

for_life_M = float(input("Введите, какой процент(%) уходит на жизнь: "))

print("На ипотеку было потрачено(руб): ", float(((salary_M / 100)*mortgage_M)*12), "руб")


print("Было накоплено: ", float((salary_M - (salary_M / 100)*mortgage_M - (salary_M / 100)*for_life_M)*12), "руб")