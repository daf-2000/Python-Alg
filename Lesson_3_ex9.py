# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random
len_1 = int(input('Введите длину строк матрицы: '))
count = int(input('Количество строк матрицы: '))
list_min = []
list_column = []
test_list = []
list_result = []
min_ = int()
matrix = [[random.randint(1,1000) for _ in range(len_1)] for i in range(count)]
for i in range(len(matrix[0])):
    for a in range(len(matrix)):
        list_column.append(matrix[a][i])

for i in range(len(list_column)):
    if i == 0:
        min_ = list_column[0]
    elif i == len(list_column) - 1:
        list_result.append(min_)
    elif i % count == 0:
        list_result.append(min_)
        min_ = list_column[i]
    elif list_column[i] >= min_:
        continue
    elif list_column[i] < min_:
        min_ = list_column[i]
for i in range(len(list_result)):
    if i == 0:
        max_ = list_result[0]
    elif list_result[i] >= max_:
        max_ = list_result[i]
    elif list_result[i] < max_:
        continue
print('Сама матрица: ')
for i in matrix:
    print(i)
print(f'Лист минимальных значений из каждгго столбца: {list_result}')
print(f'Максимальное значение среди всех минимумов по столбцам: {max_}')