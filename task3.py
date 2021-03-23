# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
from itertools import count

with open("zp.txt") as f_obj:
    lines = f_obj.readlines()
    zp = []
    for index, line in enumerate(lines, start=1):
        name, surname, salary = line.split()
        zp.append(int(salary))
        if int(salary) < 20000:
            print(surname)
    print('Average salary:', sum(zp)/index)

