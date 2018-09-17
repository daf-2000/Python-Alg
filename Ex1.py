# 1. Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив, заданный 
# случайными числами на промежутке [-100; 100). Вывести на экран исходный и отсортированный 
# массивы.

import random
arraw_base = list()
for i in range(random.randint(7,10) * 2 + 1):
    arraw_base.append(random.randint(-100,100))
print(arraw_base)
def sorted_f(arraw):
    i = int()
    arraw_old = list()
    while arraw_old != arraw:
        arraw_old = arraw.copy()
        for j in range(len(arraw) - 1):
            if arraw[j] < arraw[j + 1]:
                arraw[j], arraw[j+1] = arraw[j+1], arraw[j]
        if arraw == arraw_old:
            break
#        print(arraw)
#        print(f'OLD = {arraw_old}')
sorted_f(arraw_base)
print(arraw_base)