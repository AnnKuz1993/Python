income = float(input("Укажите значение выручки фирмы >>> "))
costs = float(input("Укажите значение издержек фирмы >>> "))
profits = income - costs
rent = profits / income
if profits > 0:
    print (f"Финансовый результат фирмы - ПРИБЫЛЬ в размере {profits}")
elif profits < 0:
    print(f"Финансовый результат фирмы - УБЫТОК в размере {profits}")
else:
    print(f"Финансовый результат фирмы - {profits}")

if profits > 0:
    print(f"Рентабельность выручки - {rent}")
else:
    print("Фирма нерентабельна")

spar = int(input("Укажите численность сотрудников фирмы >>> "))
profits_spar = profits / spar
print(f"Прибыль фирмы на одного сотрудника составляет - {profits_spar}")