"""
 Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
 В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
 преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
 и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""
import datetime
import time

class Date:
    @classmethod
    def int_date(cls, date_str: str):
        if cls.valid_date(date_str):
            date: list = date_str.split("-")[::-1]
            date = list(map(int, date))
            date_date = datetime.date(date[0], date[1], date[2])
            result = time.mktime(date_date.timetuple())
            return (result)
        return None


    @staticmethod
    def valid_date(date_str: str):
        try:
            date: list = date_str.split("-")
            date = list(map(int, date))
            if 1 <= date[0] <= 31: #проверка числа
                if 1 <= date[1] <= 12: #проверка месяца
                    if 1920 <= date[2] <= 2020: #проверка года
                        return True

        except:
            return False

print(Date.int_date("15-04-2020"))
print(Date.valid_date("15-04-2020"))
