number = int(input('Введите целое положительное число: '))
max_digit = 0
while number/10 > 0.1:
    # print((number % 10))
    number = number // 10
    if (number % 10) > max_digit:
        max_digit = number % 10
print('Самая большая цифра в числе:', max_digit)
