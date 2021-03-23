#2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
from itertools import count
with open("text.txt") as f_obj:
    lines = f_obj.readlines()
    print('Колличество строк:', len(lines))
for index, line in enumerate(lines, start=1):
    print(f'Колличество слов в строке {index}: {len(line.split())}')
