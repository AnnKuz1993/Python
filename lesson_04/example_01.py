"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
import sys
from lesson_04 import test

try:
    file, user, make, salery, prize = sys.argv
except ValueError:
    print("Invalid args")
    exit()

test.hello(user)
print(test.cal(int(make), int(salery), int(prize)))