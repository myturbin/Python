'''4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.'''


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(self.name, ' поехала')

    def stop(self):
        print(self.name, 'остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}')

    def show_speed(self):
        print(f'значение скорости {self.name}: {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police=False)
        self.is_police = False

    def show_speed(self):
        super(TownCar, self)
        print(self.speed if self.speed <= 60 else 'превышении скорости')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police=False)

    def show_speed(self):
        super(WorkCar, self)
        print(self.speed if self.speed <= 40 else 'превышении скорости')


class PoliceCar(Car):
    pass


class SportCar(Car):
    pass


vehicle1 = PoliceCar(60, 'red', 'Cop_car', False)
vehicle1.show_speed()

vehicle2 = WorkCar(50, 'white', 'John Deere', False)
vehicle2.show_speed()
vehicle2.turn('right')
vehicle2.stop()

vehicle3 = TownCar(80, 'Baklajan', 'Lada_sedan', False)
vehicle3.show_speed()

# Vopros po etoi zadache: Kak mojno sdelat atribut self.is_police default = True dlya policeiskih machin i False dlya vseh ostalnih? Spasibo!.