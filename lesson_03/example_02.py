# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_features():
    try:
        first_name = input("Введите имя пользователя: ")
        last_name = input("Введите фамилию пользователя: ")
        birthday = input("Введите год рождения пользователя: ")
        town = input("Введите город проживания пользователя: ")
        email = input("Введите e-mail пользователя: ")
        phone = input("Введите номер телефона пользователя: ")
        return print(f"Имя - {first_name}, Фамилия - {last_name}, Год рождения - {birthday}, Город проживания - {town}, E-mail - {email}, Тел. - {phone}")
    except ValueError:
        return "Не ввели значение!"

user_features()