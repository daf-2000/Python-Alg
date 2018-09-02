# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random
num_ = int(input('Введите чисмло элеметнов массива: '))
list_1 = [ random.randint(-1000,1000) for _ in range(num_) ]
min_ = list_1[0]
print(list_1)
v = 1
while v <= 2:
    for i in list_1:
        if i < min_:
            min_ = i
    print(f'minimum {v} = {min_}')
    list_1.remove(min_)
    v += 1
    min_ = list_1[0]

#Вариант2:
#list_1 = [ random.randint(-1000,1000) for _ in range(num_) ]
# def minim_(list_1):
#     min_ = list_1[0]
#     for i in list_1:
#         if i < min_:
#             min_ = i
#         else:
#             pass
#     return(min_)
# print(f'Первый минимум = {minim_(list_1)}')
# list_1.remove(minim_(list_1))
# print(f'Второй минимум = {minim_(list_1)}')