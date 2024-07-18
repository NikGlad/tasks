prime_rate = 10

region = input("Введите регион: ")
if region == "Дальний восток":
    print('ключевая ставка 2%')
    exit(1)
else:
    print("регион", region)
children = int(input("Введите колличество детей: "))

if children > 3:
    print("детей более 3, ключевая ставка", prime_rate - 1)
else:
    print("Детей менее 4", children, "ключевая ставка", prime_rate)

payroll_projekt = input("Введите, есть ли зарплатный проект в банке?: ")
if payroll_projekt == 'да':
    print("Есть зарплатный проект в банке, ключевая ставка", prime_rate - 0.5)
else:
    print("Зарплатного проекта в банке нет ", "ключевая ставка", prime_rate)

insurance = input("Введите, будет оформлена страховка в банке?: ")
if insurance == 'да':
    print("Будет оформлена страховка в банке, ключевая ставка", prime_rate - 1.5)
else:
    print("Страховка в банке не будет оформлена", "ключевая ставка", prime_rate )