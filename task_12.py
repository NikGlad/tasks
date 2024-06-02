# Мы делаем MVP dating-сервиса, и у нас есть список парней и девушек (их число может варьироваться):
#
# boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
# girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
# Выдвигаем гипотезу: лучшие рекомендации мы получим, если просто отсортируем имена по алфавиту и познакомим людей с одинаковыми индексами после сортировки!
# "Познакомить" пары нам поможет функция zip, а в цикле распакуем zip-объект и выведем информацию в виде:
#
# Идеальные пары:
# Alex и Emma
# Arthur и Kate
# John и Kira
# Peter и Liza
# Richard и Trisha
# Внимание! Если количество людей в списках будет не совпадать, то мы никого знакомить не будем и выведем пользователю предупреждение,
# что кто-то может остаться без пары!


boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Aira', 'Trisha', 'Anna']

if len(boys) == len(girls):
    print("Идеальная пара:")
    boys.sort()
    girls.sort()
    dating = zip(boys, girls)
    for company in dating:
        print(f"{company[0]} и {company[1]}")
else:

    print("Кто то может остаться без пары")