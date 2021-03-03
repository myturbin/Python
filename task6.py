dist = int(input('Введите дистанцию, которую пробежал спортсмен в первый день (в километрах): '))
aiming_dist = int(input('Введите требуемую дистанцию (в километрах): '))
print(f'1-й день: {dist}')
day = 1
while dist <= aiming_dist:
    day += 1
    print(f'{day}-й день: {round(dist * 1.1,2)}')
    dist = dist * 1.1
print(f'Ответ: на {day}-й день спортсмен достиг результата — не менее {aiming_dist} километров')
