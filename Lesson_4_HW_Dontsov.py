#100 loops, best of 5: 25.6 usec per loop ����� 100
#100 loops, best of 5: 395 usec per loop - ��� 1000
#100 loops, best of 5: 18.7 msec per loop - ��� 10000
#��� ����� ��� ���������� ����������� (��� �������� � 1000 �� 10000 ����� ����������� � 55 ���)
def fib(n):
    fib1 = 1
    fib2 = 1
    i = 2
    while i < n:
        fib_sum = fib2 + fib1
        fib1 = fib2
        fib2 = fib_sum
        i += 1

    return fib_sum
print(fib(9))
#cProfile
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.000    0.000    0.019    0.019 <string>:1(<module>)
#       1    0.000    0.000    0.019    0.019 {built-in method builtins.exec}
#       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       1    0.019    0.019    0.019    0.019 ���.py:1(fib)


#������ ���������� ������:
#>py -m timeit -n 100 -s "import FibPrim" "FibPrim.erat(1000)"
#100 loops, best of 5: 32.9 usec per loop 100 �����
#100 loops, best of 5: 350 usec per loop 1000 �����
#100 loops, best of 5: 3.55 msec per loop 10000 �����
#��� �����, ��� �������� �����������, ��� ���������� � 10 ��� ���������� �����, ����� ��� �� ������������� � 10 ���

def erat(n):
    list_1 = list(range(n + 1))
    list_1[1] = 0
    for i in list_1:
        if i > 1:
            for j in range(i + i, len(list_1), i):
                list_1[j] = 0
    return list_1
print(erat(100))
#cProfile: (�����, ��� �� ������� ��� �� ������� ���������� ���������� (0.004 vs 0.019)):
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#        1    0.004    0.004    0.004    0.004 Fib-2.py:1(erat)
#        1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#     1229    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#����� �����, ��� ������ ����� ������� �������� ��� ������, ���� � ������ ��������� �� ������ �� 1000 ����� ������������� �������.