'''5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.'''

class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):
    def draw(self):
        super(Pen, self)
        print('Запуск ручки')


class Pencil(Stationary):
    def draw(self):
        super(Pencil, self)
        print('Запуск карандаша')


class Handle(Stationary):
    def draw(self):
        super(Handle, self)
        print('Запуск маркера')


pl = Pencil('Pencil')
p = Pen('Pen')
h = Handle('Handle')

pl.draw()
p.draw()
h.draw()
