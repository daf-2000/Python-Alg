# OS -  Windows 10 Home 64

import sys


def show_size(x, level=0):
    print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for y in x.items():
                show_size(y, level + 1)

        elif not isinstance(x, str):
            for y in x:
                show_size(y, level + 1)


import random

len_1 = int(input('Введите длину строк матрицы: '))
count = int(input('Количество строк матрицы: '))
#list_min = []
list_column = []
#test_list = []
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


print('List matrix = ')
show_size(matrix)
print('List list_result = ')
show_size(list_result)
print('List list_column = ')
show_size(list_column)

print('Var min_ = ')
show_size(min_)
print('Var len_1 = ')
show_size(len_1)
print(f'Лист минимальных значений из каждгго столбца: {list_result}')
print(f'Максимальное значение среди всех минимумов по столбцам: {max_}')


# В данной программе основными потребителями памяти являются листы доступа (матрица чисел и транспонированная матрица),
# а так же список из минимумов каждого столбца.
# Сами же переменные (количемство строк и длина строк матрицы) - по сути это просто число. Можно было бы уменьшить потребление памяти программой,
# убрав операцию транспонирования матрицы. В принципе можно обойтись без этой процедуры, тогда потребности в памяти было бы меньше.
# При увеличении вводных значений в 10 раз, размер результирующей матрицы становится 268, плюс сумма размеров каждого из элементов матриц (14 * n * m)
# List matrix =
#  type = <class 'list'>, size = 52, object = [[227, 932, 278, 126, 502], [943, 298, 703, 594, 874], [602, 120, 995, 23, 831], [671, 850, 302, 873, 517]]
# 	 type = <class 'list'>, size = 68, object = [227, 932, 278, 126, 502]
# 		 type = <class 'int'>, size = 14, object = 227
# 		 type = <class 'int'>, size = 14, object = 932
# 		 type = <class 'int'>, size = 14, object = 278
# 		 type = <class 'int'>, size = 14, object = 126
# 		 type = <class 'int'>, size = 14, object = 502
# 	 type = <class 'list'>, size = 68, object = [943, 298, 703, 594, 874]
# 		 type = <class 'int'>, size = 14, object = 943
# 		 type = <class 'int'>, size = 14, object = 298
# 		 type = <class 'int'>, size = 14, object = 703
# 		 type = <class 'int'>, size = 14, object = 594
# 		 type = <class 'int'>, size = 14, object = 874
# 	 type = <class 'list'>, size = 68, object = [602, 120, 995, 23, 831]
# 		 type = <class 'int'>, size = 14, object = 602
# 		 type = <class 'int'>, size = 14, object = 120
# 		 type = <class 'int'>, size = 14, object = 995
# 		 type = <class 'int'>, size = 14, object = 23
# 		 type = <class 'int'>, size = 14, object = 831
# 	 type = <class 'list'>, size = 68, object = [671, 850, 302, 873, 517]
# 		 type = <class 'int'>, size = 14, object = 671
# 		 type = <class 'int'>, size = 14, object = 850
# 		 type = <class 'int'>, size = 14, object = 302
# 		 type = <class 'int'>, size = 14, object = 873
# 		 type = <class 'int'>, size = 14, object = 517
# List list_result =
#  type = <class 'list'>, size = 68, object = [227, 120, 278, 23, 502]
# 	 type = <class 'int'>, size = 14, object = 227
# 	 type = <class 'int'>, size = 14, object = 120
# 	 type = <class 'int'>, size = 14, object = 278
# 	 type = <class 'int'>, size = 14, object = 23
# 	 type = <class 'int'>, size = 14, object = 502
# List list_column =
#  type = <class 'list'>, size = 136, object = [227, 943, 602, 671, 932, 298, 120, 850, 278, 703, 995, 302, 126, 594, 23, 873, 502, 874, 831, 517]
# 	 type = <class 'int'>, size = 14, object = 227
# 	 type = <class 'int'>, size = 14, object = 943
# 	 type = <class 'int'>, size = 14, object = 602
# 	 type = <class 'int'>, size = 14, object = 671
# 	 type = <class 'int'>, size = 14, object = 932
# 	 type = <class 'int'>, size = 14, object = 298
# 	 type = <class 'int'>, size = 14, object = 120
# 	 type = <class 'int'>, size = 14, object = 850
# 	 type = <class 'int'>, size = 14, object = 278
# 	 type = <class 'int'>, size = 14, object = 703
# 	 type = <class 'int'>, size = 14, object = 995
# 	 type = <class 'int'>, size = 14, object = 302
# 	 type = <class 'int'>, size = 14, object = 126
# 	 type = <class 'int'>, size = 14, object = 594
# 	 type = <class 'int'>, size = 14, object = 23
# 	 type = <class 'int'>, size = 14, object = 873
# 	 type = <class 'int'>, size = 14, object = 502
# 	 type = <class 'int'>, size = 14, object = 874
# 	 type = <class 'int'>, size = 14, object = 831
# 	 type = <class 'int'>, size = 14, object = 517
# Var min_ =
#  type = <class 'int'>, size = 14, object = 502
# Var len_1 =
#  type = <class 'int'>, size = 14, object = 5