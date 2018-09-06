#4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.
import cProfile
import sys
sys.setrecursionlimit(100000)
l = 0
#n = int(input('Введите число n: '))
def summ(n, k):
    global l
    if n > 0:
        k = k / -2
        l += k
        return summ(n - 1,k)#, print(k)
    return print(f'Сумма элементов последовательности = {l}')
#summ(n, -2)

#cProfile.run("summ(100,-2)")
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#    101/1    0.001    0.000    0.001    0.001 Lesson_4-HW-ex1.py:8(summ)
#        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#
#Process finished with exit code 0

#cProfile.run("summ(1000,-2)")

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#   1001/1    0.003    0.000    0.003    0.003 Lesson_4-HW-ex1.py:8(summ)
#        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#Тут видно, что при увеличении числа n время увеличивается в меньшее количество раз (O(N))


#Результат выполнения py -m timeit -n 100 -s "import L4ex1" "L4ex1.summ(100,-2)":
#100 loops, best of 5: 778 usec per loop

# #Результат выполнения py -m timeit -n 100 -s "import L4ex1" "L4ex1.summ(1000,-2)":
#100 loops, best of 5: 2.49 msec per loop
# При дефолтных настройках ограничений по рекурсии, на вход функции если подать 1000, выдает ошибку: RecursionError: maximum recursion depth exceeded in comparison
# То-есть для больших значениях на вход, функция становится непригодна.