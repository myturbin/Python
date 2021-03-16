# 5.  У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
my_list = [7, 5, 3, 3, 2]
new_element = int(input('Введите новый элемент рейтинга: '))
c = my_list.count(new_element)
for i in range(int(len(my_list))):
    if c > 0:
        i = my_list.index(new_element)
        my_list.insert(i + c, new_element)
        break
    elif new_element > my_list[i]:
        my_list.insert(i, new_element)
        break
    elif new_element <= my_list[i-len(my_list)]:
        my_list.append(new_element)
        break

print('Обновлённый рейтинг: ', my_list)
