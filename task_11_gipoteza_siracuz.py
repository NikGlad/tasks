number = int(input('Введите число: '))

counter = 0

while number != 1:
    if number % 2 == 0:
        number /= 2
    else:
        number = (number * 3 + 1)/2
    counter += 1

print(number)
print(counter)