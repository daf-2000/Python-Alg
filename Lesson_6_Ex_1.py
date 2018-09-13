# OS -  Windows 10 Home 64

import sys


def show_size(x, level=0):
    print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for y in x.items():
                show_size(y, level + 1)

        elif not isinstance(x, str):
            for y in x:
                show_size(y, level + 1)


def mxm(num=int(input('Введите число (0 - Выход): ')), summ=0, max_1=0, level = 0):
    if num == 0:
        return print('Пока!')
    else:
        k = 0
        b = num
        print('Var num = ')
        show_size(num, level + 1)
        while num > 0:
            k = k + num % 10
            num = num // 10
            print('Funct mxm = ')
            show_size(mxm, level + 1)# Смотрим как меняется размер самой функции во время рекурсии
            print('Var k = ')
            show_size(k, level + 1)# Смотрим как меняется размер переменной суммы всех цифр текущего числа
            print('Var summ = ')
            show_size(summ, level + 1)# Смотрим как меняется размер переменной максимальной суммы цифр ранее введеных чисел
            print('Var num = ')
            show_size(num, level + 1)
            print('Var max_1 = ')
            show_size(max_1, level + 1)
        if k > summ:
            return print(f'Максимальная сумма цифр из всех введенных, в числе {b} = {k}'), mxm(int(input('Введите число: ')), k, b)
        else:
            return print(f'Максимальная сумма цифр из всех введенных, в числе {max_1} = {summ}'), mxm(int(input('Введите число: ')), summ, max_1)


mxm()

# Размер самого объекта "функция" не меняется от того, что внутри ее происходит. Меняется только размер переменных при обработке.
# Размер переменных завсист от ввода пользователя.
# В данной программе относительно постоянный элемент это переменные max_1 и summ их размер
# Эффективность использования памяти высокая, так как по факту в памяти постоянно сохраняется только максимальное число и
# сумма его цифр, осмтальное все заменяется на новые значения при каждом цикле рекурсии.
# Если посчитать сколько памяти было выделено на последнем цикле рекурсии нашей функции mxm, то получим:
# max_1 = 14, summ = 14, k = 14, num = 12 b  итого: 54


# Введите число (0 - Выход): 34
# Var num =
# 	 type = <class 'int'>, size = 14, object = 34
# Funct mxm =
# 	 type = <class 'function'>, size = 72, object = <function mxm at 0x00579E40>
# Var k =
# 	 type = <class 'int'>, size = 14, object = 4
# Var summ =
# 	 type = <class 'int'>, size = 12, object = 0
# Var num =
# 	 type = <class 'int'>, size = 14, object = 3
# Var max_1 =
# 	 type = <class 'int'>, size = 12, object = 0
# Funct mxm =
# 	 type = <class 'function'>, size = 72, object = <function mxm at 0x00579E40>
# Var k =
# 	 type = <class 'int'>, size = 14, object = 7
# Var summ =
# 	 type = <class 'int'>, size = 12, object = 0
# Var num =
# 	 type = <class 'int'>, size = 12, object = 0
# Var max_1 =
# 	 type = <class 'int'>, size = 12, object = 0
# Максимальная сумма цифр из всех введенных, в числе 34 = 7
# Введите число: 56
# Var num =
# 	 type = <class 'int'>, size = 14, object = 56
# Funct mxm =
# 	 type = <class 'function'>, size = 72, object = <function mxm at 0x00579E40>
# Var k =
# 	 type = <class 'int'>, size = 14, object = 6
# Var summ =
# 	 type = <class 'int'>, size = 14, object = 7
# Var num =
# 	 type = <class 'int'>, size = 14, object = 5
# Var max_1 =
# 	 type = <class 'int'>, size = 14, object = 34
# Funct mxm =
# 	 type = <class 'function'>, size = 72, object = <function mxm at 0x00579E40>
# Var k =
# 	 type = <class 'int'>, size = 14, object = 11
# Var summ =
# 	 type = <class 'int'>, size = 14, object = 7
# Var num =
# 	 type = <class 'int'>, size = 12, object = 0
# Var max_1 =
# 	 type = <class 'int'>, size = 14, object = 34
# Максимальная сумма цифр из всех введенных, в числе 56 = 11
# Введите число: 53
# Var num =
# 	 type = <class 'int'>, size = 14, object = 53
# Funct mxm =
# 	 type = <class 'function'>, size = 72, object = <function mxm at 0x00579E40>
# Var k =
# 	 type = <class 'int'>, size = 14, object = 3
# Var summ =
# 	 type = <class 'int'>, size = 14, object = 11
# Var num =
# 	 type = <class 'int'>, size = 14, object = 5
# Var max_1 =
# 	 type = <class 'int'>, size = 14, object = 56
# Funct mxm =
# 	 type = <class 'function'>, size = 72, object = <function mxm at 0x00579E40>
# Var k =
# 	 type = <class 'int'>, size = 14, object = 8
# Var summ =
# 	 type = <class 'int'>, size = 14, object = 11
# Var num =
# 	 type = <class 'int'>, size = 12, object = 0
# Var max_1 =
# 	 type = <class 'int'>, size = 14, object = 56
# Максимальная сумма цифр из всех введенных, в числе 56 = 11
# Введите число: 12
# Var num =
# 	 type = <class 'int'>, size = 14, object = 12
# Funct mxm =
# 	 type = <class 'function'>, size = 72, object = <function mxm at 0x00579E40>
# Var k =
# 	 type = <class 'int'>, size = 14, object = 2
# Var summ =
# 	 type = <class 'int'>, size = 14, object = 11
# Var num =
# 	 type = <class 'int'>, size = 14, object = 1
# Var max_1 =
# 	 type = <class 'int'>, size = 14, object = 56
# Funct mxm =
# 	 type = <class 'function'>, size = 72, object = <function mxm at 0x00579E40>
# Var k =
# 	 type = <class 'int'>, size = 14, object = 3
# Var summ =
# 	 type = <class 'int'>, size = 14, object = 11
# Var num =
# 	 type = <class 'int'>, size = 12, object = 0
# Var max_1 =
# 	 type = <class 'int'>, size = 14, object = 56
# Максимальная сумма цифр из всех введенных, в числе 56 = 11
# Введите число: 123
# Var num =
# 	 type = <class 'int'>, size = 14, object = 123
# Funct mxm =
# 	 type = <class 'function'>, size = 72, object = <function mxm at 0x00579E40>
# Var k =
# 	 type = <class 'int'>, size = 14, object = 3
# Var summ =
# 	 type = <class 'int'>, size = 14, object = 11
# Var num =
# 	 type = <class 'int'>, size = 14, object = 12
# Var max_1 =
# 	 type = <class 'int'>, size = 14, object = 56
# Funct mxm =
# 	 type = <class 'function'>, size = 72, object = <function mxm at 0x00579E40>
# Var k =
# 	 type = <class 'int'>, size = 14, object = 5
# Var summ =
# 	 type = <class 'int'>, size = 14, object = 11
# Var num =
# 	 type = <class 'int'>, size = 14, object = 1
# Var max_1 =
# 	 type = <class 'int'>, size = 14, object = 56
# Funct mxm =
# 	 type = <class 'function'>, size = 72, object = <function mxm at 0x00579E40>
# Var k =
# 	 type = <class 'int'>, size = 14, object = 6
# Var summ =
# 	 type = <class 'int'>, size = 14, object = 11
# Var num =
# 	 type = <class 'int'>, size = 12, object = 0
# Var max_1 =
# 	 type = <class 'int'>, size = 14, object = 56
# Максимальная сумма цифр из всех введенных, в числе 56 = 11


