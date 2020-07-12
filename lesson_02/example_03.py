# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month_list = ['зима', 'весна', 'лето', 'осень']
month_dict = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
num_month = int(input("Введите номер месяца от 1 до 12 >>> "))
if num_month == 1 or num_month == 2 or num_month == 12:
    print("Время года для этого месца >>> ", month_dict.get(1))
elif num_month == 3 or num_month == 4 or num_month == 5:
    print("Время года для этого месца >>> ", month_dict.get(2))
elif num_month == 6 or num_month == 7 or num_month == 8:
    print("Время года для этого месца >>> ", month_dict.get(3))
elif num_month == 9 or num_month == 10 or num_month == 11:
    print("Время года для этого месца >>> ", month_dict.get(4))
else:
    print("Ввели неверное число! Такого месяца не существует!")


if num_month == 1 or num_month == 2 or num_month == 12:
    print("Время года для этого месца >>> ", month_list[0])
elif num_month == 3 or num_month == 4 or num_month == 5:
    print("Время года для этого месца >>> ", month_list[1])
elif num_month == 6 or num_month == 7 or num_month == 8:
    print("Время года для этого месца >>> ", month_list[2])
elif num_month == 9 or num_month == 10 or num_month == 11:
    print("Время года для этого месца >>> ", month_list[3])
else:
    print("Ввели неверное число! Такого месяца не существует!")