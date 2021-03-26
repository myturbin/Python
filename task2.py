'''2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна.
Проверить работу метода.'''


class Road:

    def __init__(self, length, width):
        self._road_length = length
        self._road_width = width

    def asphalt_weight(self, asphalt_weight_1m2_1cm_kg, asphalt_thickness_cm):
        return print('Required asphalt weight (kg): ', self._road_length * self._road_width * asphalt_weight_1m2_1cm_kg * asphalt_thickness_cm)


road1 = Road(10, 3)

road1.asphalt_weight(1, 1)
