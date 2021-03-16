# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
# def my_f(name, surname, **kwargs):
def pers_data(name, surname, **kwargs):"""

    :param name: 
    :param surname: 
    :param kwargs: 
    :return: Stroka 
    """
    print(name, surname, kwargs)

pers_data(name='Ivan', surname= 'Ivanov', city= 'Moskva', email= 'a@a.ru', tlf= 12345)