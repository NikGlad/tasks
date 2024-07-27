# def square(number):
#     result = number ** 2
#     return result

# res = square(5)
# print(res)

# print(square(5))

# def square(number):
#     """
#     this is my function
#     """
#     result = number ** 2
#     return result

# help(square)

# def square():
#     number = int(input('Введите число'))
#     result = number ** 2
#     return result
# print(square())

# def pow(number_1, number_2):
#     result = number_1 ** number_2
#     return result
# print(pow(4, 6))

# def pow(number_1=2, number_2=5):
#     result = number_1 ** number_2
#     return result
# print(pow(6))

# def pow(number_1, number_2=2):
#     result = number_1 ** number_2
#     print(result)
#
# res = pow(6)
# print(res)

# def pow(number_1, number_2=5):
#     result = number_1 ** number_2
#     return
# print(pow(6))

# def pow(number_1, number_2=5):
#     pass

# salary = 100000
# bonus =  50000
#
# def info():
#     print(salary + bonus)
#
# info()


# salary = 100000
# bonus =  50000
#
# def info():
#     bonus = 20000
#     print(salary + bonus)
#
# info()


# salary = 100000
# bonus =  50000
#
# def info():
#     salary = 20000
#     bonus = 20000
#     some_number = 1
#     print(salary + bonus)
#
# info()
#
# print(some_number)


# def info():
#     global some_number
#     some_number = 1
#
# info()
#
# print(some_number)

# salary = 100000
# bonus =  50000
#
# def info():
#     global salary
#     salary = 20000
#
# print(salary)
# info()
# print(salary)


# my_func = lambda x, y: x**y
#
# print(my_func(6, 7))



# print(list(map(lambda x: (x**2, x**3), [252, 547, 88])))


students_list = [
    {"name": "Василий", "surname": "Тёркин", "gender": "м", "program_exp": True, "grade": [8, 8, 9, 9], "exam": 8},
    {"name": "Мария", "surname": "Павлова", "gender": "ж", "program_exp": True, "grade": [7, 8, 9, 7, 9], "exam": 9},
    {"name": "Ирина", "surname": "Андреева", "gender": "ж", "program_exp": False, "grade": [10, 9, 8, 10, 10], "exam": 7},
    {"name": "Татьяна", "surname": "Сидорова", "gender": "ж", "program_exp": False, "grade": [7, 8, 8], "exam": 10},
    {"name": "Иван", "surname": "Васильев", "gender": "м", "program_exp": True, "grade": [9, 8, 9, 6, 9], "exam": 5},
    {"name": "Роман", "surname": "Золотарев", "gender": "м", "program_exp": False, "grade": [8, 9, 9, 9], "exam": 6},
]

def get_grades(name, surname, students):
    for student in students:
        if student['name'] == name and student['surname'] == surname:
            print(', '.join(map(str, student['grade'])))

get_grades('Иван', 'Васильев', students_list)



# def get_grades(name, surname, students):
#     for student in students:
#         if student['name'] == name and student['surname'] == surname:
#             print(student['exam'])
#
# a = input('введите имя ')
# b = input('введите фамилию ')
#
# get_grades(a, b, students_list)


# def get_aw_hw_grade(students):
#     sum_hw = 0
#     for student in students:
#         sum_hw += sum(student['grade'])/len(student['grade'])
#     return sum_hw / len(students)
#
# print(get_aw_hw_grade(students_list))


# def get_aw_hw_grade(students, exp):
#     sum_hw = 0
#     counter = 0
#     for student in students:
#         if student['program_exp'] == exp:
#             sum_hw += sum(student['grade'])/len(student['grade'])
#             counter += 1
#     return sum_hw / counter
#
# print(get_aw_hw_grade(students_list, True))
# print(get_aw_hw_grade(students_list, False))
#
def get_aw_hw_grade(students, exp=None):
    sum_hw = 0
    counter = 0
    for student in students:
        if student['program_exp'] ==exp or exp is None:
            sum_hw += sum(student['grade'])/len(student['grade'])
            counter += 1
    return sum_hw / counter

print(get_aw_hw_grade(students_list))
print(get_aw_hw_grade(students_list, True))
print(get_aw_hw_grade(students_list, False))


def main(students):
    while True:
        comand = input('Введите команду ')
        if comand == '1':
            get_grades('Иван', 'Васильев', students)
        elif comand == '2':
            print(get_aw_hw_grade(students_list))
        elif comand == '3':
            print(get_aw_hw_grade(students_list, True))
        elif comand == 'q':
            print('Выход из програмы ')
            break

main(students_list)




