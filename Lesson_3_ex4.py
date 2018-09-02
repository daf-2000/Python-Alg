#4. Определить, какое число в массиве встречается чаще всего.

import random
num = int(input('Введите число элементов массива: '))
list_1 = [random.randint(1, 10) for _ in range(num)]
count = 0
list_count = list()
for i in list_1:
    for k in list_1:
        if i == k:
            count += 1
    list_count.append(count)
    count = 0
max_ = 0
for i in list_count:
        if i > max_:
            max_ = i
print(list_1)
#print(list_count)
print(f'Чаще всего в листе встречается число {list_1[list_count.index(max_)]} и оно встречается {max_} раз')