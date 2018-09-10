import collections
x = input('a = ').upper()
y = input('b = ').upper()
#dict_1 = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
#dict_2 = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
dict_2 = {x: chr(y) for x, y in zip(range(10,16), range(65,71))}
dict_1 = {chr(y): x for y, x in zip(range(65,71), range(10,16))}


def summ(x,y):#Функция для сложения 16-ричных цифр
    list_1 = list()
    if x in dict_1:
        x = dict_1[x]
    else:
        x = int(x)
    if y in dict_1:
        y = dict_1[y]
    else:
        y = int(y)
    z = x + y
    if z > 15:
        if z - 16 > 9:
            list_1.append(1)
            list_1.append(dict_2[z - 16])
        else:
            list_1.append('1')
            list_1.append(z - 16)
    else:
        list_1.append(z if z <= 9 else dict_2[z])

    return list_1


list_x = collections.deque(x)
list_y = collections.deque(y)
list_last = collections.deque()


def summ_res(list_x, list_y):#Функция для сложения шестнадцатиричных чисел
    list_result = collections.deque()
    if len(list_x) > len(list_y):#Приводим листы к одному размеру, чтоб удобнее было складывать по разрядам (можно было и по индексам, конечно)
        while len(list_x) > len(list_y):
            list_y.appendleft(0)
    elif len(list_y) > len(list_x):
        while len(list_y) > len(list_x):
            list_x.appendleft(0)
    for i in range(len(list_x)):
        list_result.append(summ(list_x[i], list_y[i]))
    list_result.appendleft([0])#list_result содержит в себе сумму разрядов каждого числа
    k = 0
    while k < len(list_result):#там где разряд получился двойной, переводим в разряд выше
        k += 1
        for i in range(len(list_result)):
            if len(list_result[i]) == 2:
                list_result[i - 1] = summ(list_result[i - 1][0], list_result[i][0])
                list_result[i] = [list_result[i][1]]
    for i in range(len(list_result)):
        list_result[i] = list_result[i][0]
    if list_result[0] == 0:
        list_result.popleft()
    return collections.deque(list_result)


print(f'Результат сложения = {list(summ_res(list_x, list_y))}')
######## mult
list_m_x = collections.deque(x)
list_m_y = collections.deque(y)
list_m_result = collections.deque()


def mult(x, y):
    if x in dict_1:
        x = dict_1[x]
    else:
        x = int(x)
    if y in dict_1:
        y = dict_1[y]
    else:
        y = int(y)
    z = x * y#Тут можно было конечно обойтись без вычислений, а подставить значение из словаря таблицы умножения )
    z_1 = z // 16
    z_2 = z % 16
    if z_1 > 9:
        z_1 = dict_2[z_1]
    if z_2 > 9:
        z_2 = dict_2[z_2]
    return [z_1,z_2] if z_1 != 0 else [z_2]


for i in range(len(list_m_x)):
    for j in range(len(list_m_y)):
        list_m_result.append(collections.deque(mult(list_m_x[i],list_m_y[j]) + [0] * ((len(list_m_x) - 1 - i) + (len(list_m_y) -1 - j))))
# Складываем результат умножения каждого разряда
mult_res = list_m_result[0]
for i in range(1,len(list_m_result)):
    mult_res = summ_res(mult_res, list_m_result[i])
print(f'Результат умножения = {mult_res}')


