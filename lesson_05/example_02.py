"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке
"""

my_file = open(r'example_02', "w")
my_list = ['Hello!\n', 'The weather is nice today\n', 'Shall we go out?\n']
lines = 0
flag = 0
words = 0
for i in my_list:
    lines += 1

    for j in i:
        if j != ' ' and flag == 0:
            words += 1
            flag = 1
        elif j == ' ':
            flag = 0

    print(i, 'В строке', len(i), 'символов', words, 'слов')

print('Всего в файле',lines, 'строки')
my_file.close()
