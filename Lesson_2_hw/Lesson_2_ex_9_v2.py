# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

def mxm(num = int(input('Введите число (0 - Выход): ')), summ = 0, max_1 = 0):
   if num == 0:
       return print('Пока!')
   else:
       k = 0
       b = num
       while num > 0:
                k = k + num % 10
                num = num // 10
       if k > summ:
            return print(f'Максимальная сумма цифр из всех введенных, в числе {b} = {k}'), mxm(int(input('Введите число: ')), k, b)
       else:
          return print(f'Максимальная сумма цифр из всех введенных, в числе {max_1} = {summ}'), mxm(int(input('Введите число: ')), summ, max_1)
mxm()