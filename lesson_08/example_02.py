"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
"""
class MyZeroDivisionError(Exception):
    zero_error = "На ноль делить нельзя!"

class UserException:
    def __init__(self, args: int):
        self.args = args

    def __truediv__(self, other):
        if other.args == 0:
            raise MyZeroDivisionError
        else:
            print(self.args / other.args)

user_int_1 = UserException(int(input("Введите числитель: ")))
user_int_2 = UserException(int(input("Введите знаменатель: ")))


try:
    result = user_int_1 / user_int_2
except MyZeroDivisionError as my_error:
    print(my_error.zero_error)
