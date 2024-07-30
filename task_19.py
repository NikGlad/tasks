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

comand = input("Введите команду ")

def p_people(number, peoples):
    for people in peoples:
        if people['number'] == number:
            print(people['name'])

num = input('введите номер документа ')

p_people(num, documents)

def main():
    while True:
        if comand == 'p':
            p_people(num, documents)


