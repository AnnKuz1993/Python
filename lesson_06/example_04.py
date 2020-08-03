"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""


class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed != 0:
            print("Машина поехала!")

    def stop(self):
        if self.speed == 0:
            print("Машина остановилась!")

    def turn(self, direction):
        if direction == 1:
            print("Машина повернула налево!")
        if direction == 2:
            print("Машина повернула направо!")

    def show_speed(self):
        print(f"Скорость движения = {self.speed}")


class TownCar(Car):
    title: str

    def __init__(self, speed, color, name, title=True):
        super().__init__(speed, color, name)
        self.title = title

    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости!")
        else:
            print(f"Скорость движения = {self.speed}")


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости!")
        else:
            print(f"Скорость движения = {self.speed}")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


toyota = TownCar(70, "black", "Toyota")
print(toyota.name, toyota.color, toyota.speed)
toyota.go()
toyota.turn(2)
toyota.show_speed()
audi = SportCar(80, "rad", "Audi")
print(audi.name, audi.color, audi.speed)
audi.go()
audi.turn(1)
audi.show_speed()
ford = WorkCar(50, "green", "Ford", True)
print(ford.name, ford.color, ford.speed)
ford.go()
ford.turn(2)
ford.show_speed()
renault = PoliceCar(70, "black", "Renault")
print(renault.name, renault.color, renault.speed)
renault.go()
renault.turn(2)
renault.show_speed()
