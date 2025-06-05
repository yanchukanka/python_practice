# принимаю на вход кол-во строк и столбцов
n, m = int(input()), int(input())

# заполняю матрицу данными на вход. они пока что имеют тип str
matrix = []
for i in range(n):
    matrix.append(input().split())

# берем произвольный максимальный элемент, например, самый первый
max_num = int(matrix[0][0])
row_max = 0  # переменные для будущего вывода нужной строки и столбца
column_max = 0

# идем по всей матрице и сравниваем каждый элемент с максимальным типа int. каждый бОльший присваиваем
# в переменную max_num
for r in range(n):
    for c in range(m):
        if int(matrix[r][c]) > int(max_num):
            max_num = matrix[r][c]
            row_max = r
            column_max = c

print(row_max, column_max)