# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
with open("digits.txt", 'w') as f_obj:
    digits = input('Введите числа через пробел: ')
    f_obj.write(digits)
    numbers = map(int, digits.split())
    print(sum(numbers))

