name = input("Привет! Как тебя зовут >>> ")
age = int(input("А сколько тебе лет >>> "))
print(f"Приятно познакомится,{name}! Не ожидала, что тебе {age}")

print("Давай посчитаем площадь трапеции,",name)
num_1 = int(input("Введи длину первого основания >>> "))
num_2 = int(input("Введи длину второго основания >>> "))
num_3 = int(input("А теперь укажи высоту трапеции >>> "))
S = (num_1 + num_2) * num_3 / 2
print("Площадь нашей трапеции составит: ",S)
