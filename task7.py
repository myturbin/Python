# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json

with open("firms.txt") as f_obj1:
    firms = dict()
    avg_profit = []
    lines = f_obj1.readlines()
    for line in lines:
        firm_name, firm_type, revenue, cost = line.split()
        costs = cost.replace('.', '')
        profit = int(revenue) - int(costs)
        firms[firm_name] = profit
        if profit > 0:
            avg_profit.append(profit)
    average_profit = round(sum(avg_profit) / len(avg_profit))
    output = [firms, {'average_profit': average_profit}]

    with open('output7.json', 'w') as f_json:
        json.dump(output, f_json)

    with open('output7.json') as f_json:
        print(json.load(f_json))





