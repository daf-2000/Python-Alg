#3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найти в 
#массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в 
#одной находятся элементы, которые не меньше медианы, в другой – не больше ее.
#
#Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то #используйте метод сортировки, который не рассматривался на уроках.

import random
mr = 0
lt = 0
eq = 0
arraw_base = list()
for i in range(random.randint(2,3) * 2 + 1):
    arraw_base.append(random.randint(-30,30))
print(arraw_base)
for i in range(len(arraw_base)):
    for j in range(len(arraw_base)):
        if i == j:
            continue
        elif arraw_base[i] > arraw_base[j]:
            mr += 1
        elif arraw_base[i] < arraw_base[j]:
            lt += 1
        else:
            eq += 1
#    print(mr, lt, eq)
    if lt == mr:
        print(f'Mediana = {arraw_base[i]}')
        lt = 0
        mr = 0
        eq = 0
        break
    for k in range(0,eq + 1):
        if lt + (eq - k) == mr + k or mr + (eq - k) == lt + k:
            print(f'Mediana = {arraw_base[i]}')
            eq = 0
            lt = 0
            mr = 0
            break
    else:
        lt = 0
        mr = 0
        eq = 0
