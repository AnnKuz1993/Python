"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position
(должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position
(должность) на базе класса Worker. В классе Position реализовать методы получения полного имени
сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу примера
на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
вызвать методы экземпляров)
"""

class Worker:
    name: str
    surname: str
    wage: int
    bonus: int

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
    def get_full_name(self):
        return f"Здравствуйте, {self.name} {self.surname},"
    def get_total_income(self):
        self._income = {"wage": self.wage, "bonus": self.bonus}
        total = self.wage + self.bonus
        return f"ваш доход с учетом премии составляет {total} р."

liza = Position("Лиза", "Иванова", "Architect", 30000, 10000)
print(liza.get_full_name(), liza.get_total_income())