number = int(input('Введите время в секундах: '))
hours = number // 3600
minutes = (number - (hours*3600)) // 60
seconds = number - (hours*3600) - (minutes*60)
print(f' {hours}:{minutes}:{seconds}')
