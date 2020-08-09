"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
— одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
(2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    title: str

    def __init__(self, title: str):
        self.title = title

    @property
    @abstractmethod
    def expense_material(self):
        pass

class Coat(Clothes):
    size: float

    def __init__(self, title: str, size: float):
        super().__init__(title)
        self.size = size

    @property
    def expense_material(self):
        print(f"Расход ткани для пальто {self.title} размера {self.size} составит:", self.size / 6.5 + 0.5, "м.")

class Costume(Clothes):
    growth: float

    def __init__(self, title: str, growth: float):
        super().__init__(title)
        self.growth = growth

    @property
    def expense_material(self):
        print(f"Расход ткани для костюма {self.title} с ростом  {self.growth} м. составит:", 2 * self.growth + 0.3, "м.")


coat1 = Coat("'Coat_124'", 44)
print(coat1.expense_material)

customer1 = Costume("'Custome_445'", 1.64)
print(customer1.expense_material)