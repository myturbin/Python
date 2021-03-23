# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
from functools import reduce

with open("study.txt", encoding='utf-8') as f_obj1:
    subjects = dict()
    lines = f_obj1.readlines()
    for line in lines:
        subject_name, subject_data = line.split(':')
        subject_data1 = subject_data.replace('(л)', '')
        subject_data2 = subject_data1.replace('(лаб)', '')
        subject_data3 = subject_data2.replace('(пр)', '')
        subject_data4 = subject_data3.replace('—', '')
        subject_data5 = subject_data4.replace('.', '')
        subjects[subject_name] = reduce(lambda x, y: int(x) + int(y), subject_data5.split())
print(subjects)
