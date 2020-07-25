"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
(не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих
сотрудников. Выполнить подсчет средней величины дохода сотрудников
"""

with open('example_03.txt', 'r', encoding='utf-8') as my_file:
    my_dict = {}
    try:
        for line in my_file:
            key, value = line.split()
            my_dict[key] = value
            if float(value) < 20000:
                print(f"{key}: зарплата меньше 20000 и составляет {value}")
    except ValueError:
        print("")

total = sum(map(float, my_dict.values()))
count_dict = len(my_dict)
avr = total / count_dict
print(f"Средняя величина доходов сотрудников: {avr}")
