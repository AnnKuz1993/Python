"""
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать
данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь
со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджер контекста.
"""
import json

firm_profit = {}
profit = {}
data = [firm_profit, profit]
sum_prof = 0
count_firm = 0

with open('example_07', 'r') as firms:
    for line in firms:
        name, form, count, cost = line.split()
        prof = float(count) - float(cost)
        firm_profit[name] = prof
        if prof > 0:
            count_firm = count_firm + 1
            sum_prof = sum_prof + prof

if count_firm > 0:
    profit["average_profit"] = sum_prof / count_firm

with open("example_07.json", "w") as firms_write:
    json.dump(data, firms_write)
print(f"{firm_profit}, {profit}")