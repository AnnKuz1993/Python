# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент
# с тем же значением должен разместиться после них.

my_list = [7,5,3,3,2]
print(f"Задан следующий рейтинг >>> {my_list}")
user_num = int(input("Введите новый элемент рейтинга >>> "))

for el in range(len(my_list)):
    if my_list[el] == user_num:
        my_list.insert(el + 1, user_num)
        break
    elif my_list[0] < user_num:
        my_list.insert(0, user_num)
    elif my_list[-1] > user_num:
        my_list.append(user_num)
    elif my_list[el] > user_num and my_list[el + 1] < user_num:
        my_list.insert(el + 1, user_num)
print(f"Новый рейтинг >>> {my_list}")
