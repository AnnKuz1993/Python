"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

user_file = open("user_file.txt", 'w')

while True:
    user_el = []
    user_answer = input("Введите любые данные для записи в текстовый файл 'user_file.txt' либо 'Enter' для выхода: ")
    if user_answer == '':
        break

    for el in range(user_answer.count(' ')):
        user_el = user_answer.split()

        user_file.write('\n'.join(user_el))

user_file.close()
