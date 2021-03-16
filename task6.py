# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
goods = []
features = {'название товара': '', 'цена': '', 'количество': '', 'eд': ''}
analytics = {'название товара': [], 'цена': [], 'количество': [], 'eд': []}
num = 0
while True:
    control = input("Для выхода нажмите 'Q', для продолжнения нажмите  'Enter'").upper()
    if control == 'Q':
        break
    num += 1
    for f in features.keys():
        user_data = input(f'{f}: ')
        features[f] = int(user_data) if (f == 'цена' or f == 'количество') else user_data
        analytics[f].append(features[f])
    goods.append((num, features.copy()))
    print('Аналитика:')
    for key, value in analytics.items():
        print(key, value)
# Priznayus chesno etu zadachu ya sam ne smog reshit i podtsmotrtel u vas