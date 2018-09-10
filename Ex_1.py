import collections
dict_1 = collections.defaultdict(list)
num_com = int(input('Введите количество предприятий: '))
list_q = list()
list_prof = list()
prof = float()
m = float()
list_up = list()
list_down = list()
for i in range(num_com):
    name = input(f'Введите имя компании {i+1}: ')
    for j in range(5):
        if j == 4:
            for k in list_q:
                m += k
                prof += k
            list_q.append(m)
            dict_1[name] = list_q
            list_q = list()
            m = float()
            break
        list_q.append(float(input(f'Введите прибыль приедприятия {name} за {j + 1} квартал')))
print(f'Средняя годовая прибыль по всем предприятиям: {prof / num_com}')
for key,value in dict_1.items():
    if value[4] > prof / num_com:
        list_up.append(key)
    if value[4] < prof / num_com:
        list_down.append(key)
for i in list_up:
    print(f'Предприятие {i}, прибыль выше среднего показателя за год. Прибыль составляет {dict_1[i][4]}')
for i in list_down:
    print(f'Предприятие {i}, прибыль ниже среднего показателя за год. Прибыль составляет {dict_1[i][4]}')


