"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
 а также других данных, можно использовать любую подходящую структуру, например словарь.

Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
 изученных на уроках по ООП.
"""
from enum import Enum

class type_tech(Enum):
    printer = "Принтер"
    scaner = "Сканер"
    copier = "Ксерокс"

class Org_tech():
    def __init__(self, price:int, size: list, id: int, type: type_tech):
        self.price = price
        self.id = id
        if len(size) == 3:
            self.size = size
        else:
            print("Кол-во переменных в list size должно быть 3")
            exit()


    def __str__(self):
        return "оборудование с id " + str(self.id)
class Warehouse:
    max_tech_war = 50
    current_value = 0
    max_size = [70, 70, 70]
    current_tech = []

class Directions(Enum):
    warehouse = "Склад орг.техники"
    sale = "Продажи"
    logist = "Логистика"
    buch = "Бухгалтерия"

class Office:
    current_tech = []

class userTechNotFound(Exception):
    errorName = "Оборудование не найдено"

class userTechNotEnoughSize(Exception):
    maxSize: int
    errorName = ""
    def __init__(self, size: Warehouse.max_size):
        self.maxSize = size
        self.errorName = f"Размер не соответствует ({self.maxSize})"


class Operations():
    @classmethod
    def moveEqupment(cls, office: Office, warehouse: Warehouse,
                     equipmentID: int, targetTo: Directions):
        if targetTo == Directions.warehouse:
            found = False
            indexEq = None
            for num in warehouse.current_tech:
                if num.id == equipmentID:
                    indexEq = warehouse.current_tech.index(num)
                    found = True
            if not found:
                raise userTechNotFound
            elif found:
                office.current_tech.append(warehouse.current_tech[indexEq])
                del warehouse.current_tech[indexEq]
                print("Успешно")

War_1 = Warehouse()
Office_1 = Office()

War_1.current_tech.append(Org_tech(114, [20, 10, 30], 94, type_tech.scaner))
War_1.current_tech.append(Org_tech(12, [60, 10, 40], 94, type_tech.printer))
print(f"Количество оборудования на складе: {len(War_1.current_tech)}")
Operations.moveEqupment(Office_1, War_1, 122, Directions.logist)
print(f"кол-во текущего оборудования на складе после операции: {len(War_1.current_tech)}")
print(f"кол-во текущего оборудования в офисе после операции: {len(Office_1.current_tech)}")