# Разделитель. Пользователь вводит какой-нибудь символ. Нужно разделить первую задачу и вторую задачу строкой из этого символа.
# Длина строки должна быть суммой периметра квадрата и площади прямоугольника.
#   Пример:
#   #
#   Вывод:
#   ########################

square = float(input("Введите длину стороны квадрата: "))

print("Периметр квадрата: ", float(square*4))

rectangle_l = float(input("Введите длину стороны прямоугольника: "))
rectangle1_w = float(input("Введите ширину стороны прямоугольника: "))


print("Площадь прямоугольника: ", float(rectangle_l * rectangle1_w))

simbol = input()

# summ_simbol = simbol * ((square*4) + (rectangle_l * rectangle1_w))

print(simbol * int((square*4) + (rectangle_l * rectangle1_w)))