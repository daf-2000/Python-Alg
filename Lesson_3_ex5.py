#5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random
num = int(input('Введите число элементов массива: '))
list_1 = [random.randint(-100, 100) for _ in range(num)]
max_ = 0
for i in list_1:
    if i < 0:
        if max_ == 0:
            max_ = i
        elif i > max_:
            max_ = i
print(list_1)
print(f'Максимальный элемент из всех отрицательных = {max_}')