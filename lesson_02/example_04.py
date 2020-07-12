# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

user_string = input('Введите любую фразу (через пробел) >>> ')
user_el = []
num = 1
for el in range(user_string.count(' ') + 1):
    user_el = user_string.split()
    if len(str(user_el)) <= 10:
        print(f" {num} {user_el [el]}")
        num += 1
    else:
        print(f" {num} {user_el[el][0:10]}")
        num += 1

