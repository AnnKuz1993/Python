"""
 Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться
 сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
 Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится
 специальный символ, выполнение программы завершается. Если специальный символ введен после нескольких чисел,
 то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""

def user_sum():
    sum_nums = 0
    while True:
        nums = input("Введите несколько чисел через пробел либо '!' для выхода: ").split()
        for el in nums:
            try:
                if el == "!":
                    print(f"Итоговая сумма веденных чисел составила = {sum_nums}. Работа завершена!")
                    return
                else:
                    sum_nums += int(el)
            except ValueError:
                print("Введите числа или '!' для выхода!")
        print(f"Сумма введенных чисел равна = {sum_nums}")

user_sum()