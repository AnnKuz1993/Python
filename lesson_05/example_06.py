"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
лекционных, практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий
название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
my_dict = {}
with open('example_06.txt', 'r', encoding='utf-8') as my_file:
    try:
        for line in my_file:
            clear_line = line.replace("(л)", "").replace("(пр)", "").replace("(лаб)", "").replace(":", "")
            subject, lecture, practice, lab = clear_line.split()
            lectInt = 0
            practiceInt = 0
            labInt = 0
            if lecture != "-":
                lectInt = int(lecture)
            if practice != "-":
                practiceInt = int(practice)
            if lab != "-":
                labInt = int(lab)
            my_dict[subject] = lectInt + practiceInt + labInt

            print(f"{my_dict}")

    except ValueError:
        print("")
