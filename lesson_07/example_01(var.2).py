class Matrix(object):
    value: list = []

    def __init__(self, value: list):
        self.value = value

    def __add__(self, other: 'Matrix'):
        try:
            rows_count = len(self.value)
            items_count = len(self.value[0])

            new_value = [
                [
                    self.value[row][idx] + other.value[row][idx]
                    for idx in range(items_count)
                ]
                for row in range(rows_count)
            ]

            return Matrix(new_value)
        except IndexError:
            print("Ошибка - Матрицы разного размера")
            exit(1)

    def __str__(self):
        return "\n".join(
            str(row).strip('[]').replace('.', '')
            for row in self.value
        )

mat1 = Matrix([
    [11, 12, 13],
    [14, 15, 16]
])

mat2 = Matrix([
    [21, 22, 23],
    [24, 25, 26]
])

print(mat1 + mat2)