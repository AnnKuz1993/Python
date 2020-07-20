# итератор, генерирующий целые числа, начиная с указанного
from itertools import count

for el in count (3):
    if el > 10:
        break
    else:
        print(el)
# итератор, повторяющий элементы некоторого списка, определенного заранее
from itertools import cycle

c = 0
for el in cycle("ABBY"):
    if c > 7:
        break
    print(el)
    c += 1
