num = int(input("Введите любое целое положительное число >>> "))
ost = num % 10
num = num // 10
while num > 0:
    if num % 10 > ost:
        ost = num % 10
    num = num // 10
print("Самая большая цифра в числе - это ", ost)