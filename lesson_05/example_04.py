"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""
f2 = open('example_04_v2.txt', 'w')
my_list = ["Один", "Два", "Три", "Четыре"]
n = 0

for k in open('example_04.txt'):
    p = k.split(' - ')
    p.pop(0)
    p.insert(0, my_list[1])
    p = ' - '.join(p)
    f2.write(p + '\n')
    n += 1

f2.close()
