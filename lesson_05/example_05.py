"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
file_list = [12, 55, 101, 16, 59, 321, 2]
new_list = [str(i) + ' ' for i in file_list]
with open(r'example_05.txt', 'w') as my_file:
    my_file.writelines(new_list)
    result = [int(item) for item in new_list]
    print(sum(result))

