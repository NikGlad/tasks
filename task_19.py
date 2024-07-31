# Я работаю секретарем и мне постоянно приходят различные документы.
# Я должен быть очень внимателен чтобы не потерять ни один документ. Каталог документов хранится в следующем виде:
# Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:
#
# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.
# Внимание: p, s, l, a - это пользовательские команды, а не названия функций. Функции должны иметь выразительное название, передающие её действие.

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def get_name(docs, number):
    documents = list(filter(lambda x: x['number'] == number, docs))
    if documents:
        return documents[0]['name']
    else:
        return 'Документа с таким номером нет'


def get_shelf(dirs, number):
    for key, value in dirs.items():
        if number in value:
            return key
    return 'В полках документа с данным номером нет.'


def get_list(docs):
    for doc in docs:
        print(doc['type'], doc['number'], doc['name'])


def add_doc(docs, shelfs, shelf, type, number, name):
    doc = {'type': type, 'number': number, 'name': name}
    docs.append(doc)
    shelfs[shelf].append(doc['number'])
    return 'Документ добавлен'



while True:
    print('Возможные команды: p, s, l, a')
    comand = input('Введите название команды ')

    if comand == 'p':
        num = input('Введите номер документа ')
        print(get_name(documents, num))

    elif comand == 's':
        num = input('Введите номер документа ')
        print(get_shelf(directories, num))

    elif comand == 'l':
        get_list(documents)

    elif comand == 'a':
        shelf = input('Введите номер полки куда положить документ. ')
        if shelf in directories.keys():
            type = input('Введите тип документа. ')
            number = input('Введите номер документа. ')
            name = input('Введите имя владельца документа ')
            add_doc(documents, directories, shelf, type, number, name)
        else:
            print("Номер полки введен не верно")