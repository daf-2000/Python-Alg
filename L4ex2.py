import math
import cProfile
def simple(n):
    dict_1 = dict()
    dict_1[1], dict_1[2] = 2, 3
    i = 2
    cnt = 3
    while cnt <= n:
        for j in range(2,int(math.sqrt(i)) + 1):
            if i % j == 0:
                break
            elif i % j != 0 and j ==  int(math.sqrt(i)):
                dict_1[cnt] = i
                cnt += 1
        i +=1
    return dict_1
#print('Ниже информация cProfile для самописного агоритма по нахождению простых чисел (для нахождения сотого числа):')
#cProfile.run('simple(100)')
#print('Ниже информация cProfile для самописного агоритма по нахождению простых чисел (для нахождения тысячного числа):')
#cProfile.run('simple(1000)')


def erat(n):
    list_1 = list(range(n + 1))
    list_1[1] = 0
    for i in list_1:
        if i > 1:
            for j in range(i + i, len(list_1), i):
                list_1[j] = 0
    return list_1
import cProfile
#print('Ниже информация cProfile для агоритма "Решето Эратосфена" по нахождению простых чисел (для нахождения сотого числа):')
#cProfile.run('erat(100)')
#print('Ниже информация cProfile для агоритма "Решето Эратосфена" по нахождению простых чисел (для нахождения тысячного числа):')
#cProfile.run('erat(1000)')

#Ниже информация cProfile для самописного агоритма по нахождению простых чисел (для нахождения сотого числа):
#         2441 function calls in 0.008 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.008    0.008 <string>:1(<module>)
#        1    0.006    0.006    0.008    0.008 Simple.py:3(simple)
#        1    0.000    0.000    0.008    0.008 {built-in method builtins.exec}
#     2437    0.002    0.000    0.002    0.000 {built-in method math.sqrt}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#Ниже информация cProfile для самописного агоритма по нахождению простых чисел (для нахождения тысячного числа):
#         86628 function calls in 0.250 seconds - результат больше в 31 раз, а номер больше всего в 10 раз. Функция имеет алгоритм сложности O(N*30)
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.250    0.250 <string>:1(<module>)
#        1    0.196    0.196    0.250    0.250 Simple.py:3(simple)
#        1    0.000    0.000    0.250    0.250 {built-in method builtins.exec}
#    86624    0.054    0.000    0.054    0.000 {built-in method math.sqrt}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#Ниже информация cProfile для агоритма "Решето Эратосфена" по нахождению простых чисел (для нахождения сотого числа):
#         29 function calls in 0.000 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 Simple.py:23(erat)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       25    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#Ниже информация cProfile для агоритма "Решето Эратосфена" по нахождению простых чисел (для нахождения тысячного числа):
#         172 function calls in 0.001 seconds - видно что время увечичивается прямо пропорционально (и количество раз вызова функции тоже)
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#        1    0.001    0.001    0.001    0.001 Simple.py:23(erat)
#        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#      168    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# РЕЗУЛЬТАТ ВЫПОЛНЕНИЯ КОМАНДЫ py -m timeit -n 100 -s "import Simple" "Simple.simple(100)":
#100 loops, best of 5: 6.3 msec per loop
# РЕЗУЛЬТАТ ВЫПОЛНЕНИЯ КОМАНДЫ py -m timeit -n 100 -s "import Simple" "Simple.simple(1000)":
#100 loops, best of 5: 198 msec per loop
#Тут видно, что зависимость далеко не линейная (но и не квадратичная, результат приблизительно в 30 раз больше, а число на вход в 10)


# РЕЗУЛЬТАТ ВЫПОЛНЕНИЯ КОМАНДЫ py -m timeit -n 100 -s "import Simple" "Simple.erat(100)":
#100 loops, best of 5: 96.3 usec per loop
# РЕЗУЛЬТАТ ВЫПОЛНЕНИЯ КОМАНДЫ py -m timeit -n 100 -s "import Simple" "Simple.erat(1000)":
#100 loops, best of 5: 1.09 msec per loop

#Во второй функции четко прослеживается линейная зависимость от значения подаваемого на вход функции
#Явно видно, что второй вариант алгоритма более быстрый.