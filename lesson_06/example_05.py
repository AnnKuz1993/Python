"""
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
метод для каждого экземпляра
"""

class Stationery:
    title: str
    
    def __init__(self, title):
        self.title = title
        
    def draw(self):
        print("Запуск отрисовки.")
        
class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
        
    def draw(self):
        print("Рисуем ручкой!")

class Pencil(Stationery):
    def draw(self):
        print("Рисуем карандашом!")

class Handle(Stationery):
    def draw(self):
        print("Рисуем маркером!")

pen1 = Pen("Ручка 'ССТ'")
print(pen1.title)
pen1.draw()
pencil1 = Pencil("Карандаш 'ОТР'")
print(pencil1.title)
pencil1.draw()
hendle1 = Handle("Карандаш 'ОТР'")
print(hendle1.title)
hendle1.draw()