# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
month = int(input('Введите месяц в виде целого числа от 1 до 12: '))
seasons = ['зима', 'весна', 'лето', 'осень']
if month == 12 or 1 or 2:
    print('Это', seasons[0])
elif month == 3 or 4 or 5:
    print('Это', seasons[1])
elif month == 6 or 7 or 8:
    print('Это', seasons[2])
elif month == 9 or 10 or 11:
    print('Это', seasons[3])
elif month > 12 or month < 1:
    print(' Такого месяца нет!')
