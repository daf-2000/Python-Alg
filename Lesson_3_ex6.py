# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random
num = int(input('Введите число элементов массива: '))
list_1 = [random.randint(-100, 100) for _ in range(num)]
min_ = list_1[0]
max_ = list_1[0]
print(list_1)
for i in list_1:
    if i < min_:
        min_ = i
    elif i > max_:
        max_ = i
summ = 0
print(f'Минимальный элемент списка равен = {min_}, Максимальный элемент списка равен = {max_}')
if list_1.index(max_) > list_1.index(min_):
    for i in range(list_1.index(min_) + 1, list_1.index(max_)):
        summ += list_1[i]
else:
    for i in range(list_1.index(max_) + 1, list_1.index(min_)):
        summ += list_1[i]
print(f'Сумма элементов списка, между максимальным и минимальным элементом, равна = {summ}')