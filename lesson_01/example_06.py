a = float(input("Введи результат пробежки в 1-ый день: "))
b = float(input("Введи желаемый результат пробежки: "))
day = 0
while a < b:
    a = a * 1.1
    day += 1
print("Ты достигнешь желаемого результата на ",day,"-й день")
