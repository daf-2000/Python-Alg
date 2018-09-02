#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random
num = int(input('Введите число элементов массива: '))
list_1 = [random.randint(-100, 100) for _ in range(num)]
min_ = list_1[0]
max_ = list_1[0]
for i in list_1:
    if i < min_:
        min_ = i
    elif i > max_:
        max_ = i
print(list_1)
print(f'Минимальный элемент = {min_}, Максимальный = {max_}')
ind_min = list_1.index(min_)
ind_max = list_1.index(max_)
list_1[ind_min], list_1[ind_max] = list_1[ind_max], list_1[ind_min]
print(list_1)