'''1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.'''
import time


class TrafficLight:
    def __init__(self):
        self.__color = ['Red', 'Yellow', 'Green']

    def running(self):
        while True:
            print(self.__color[0:1])
            time.sleep(7)
            print(self.__color[1:2])
            time.sleep(2)
            print(self.__color[2:3])
            time.sleep(1)


tr_light1 = TrafficLight()
tr_light1.running()

# kak osushestvit s 'cycle' ya ne soobrazil