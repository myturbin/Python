# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
def my_func(n1, n2, n3):"""
    :param n1: 
    :param n2: 
    :param n3: 
    :return: sum of 2 max numbers
    """
    answer = (n1 + n2 + n3) - min(n1, n2, n3)
    return answer

