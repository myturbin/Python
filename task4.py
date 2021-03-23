# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

with open("input4.txt", encoding='utf-8') as f_obj1:
    rus_dig = ['один', 'два', 'три', 'четыре']
    lines = f_obj1.readlines()

with open("output4.txt", "w", encoding='utf-8') as f_obj2:
    for index, line in enumerate(lines):
        if '1' in line:
            line = line.replace('One', rus_dig[index])
        elif '2' in line:
            line = line.replace('Two', rus_dig[index])
        elif '3' in line:
            line = line.replace('Three', rus_dig[index])
        elif '3' in line:
            line = line.replace('Four', rus_dig[index])
        f_obj2.write(line)
