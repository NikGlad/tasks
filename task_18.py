# Напишите код для преобразования произвольного списка вида
# ['2018-01-01', 'yandex', 'cpc', 100]
# (он может быть любой длины) в словарь
# {'2018-01-01': {'yandex': {'cpc': 100}}}

a = ['2018-01-01', 'yandex', 'cpc', 100]

storage = {}

for b in a:
    b = a[0]
for c in a:
    c = a[1]
for d in a:
    d = a[2]
for e in a:
    e = a[3]

storage1 = {d, e}

storage2 = {c : storage1}

storage = {b : storage2}





print(storage)