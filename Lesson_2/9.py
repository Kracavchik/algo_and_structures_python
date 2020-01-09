"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""

import sys


def max_number(number_1: int, number_2: int):
    """Принимает два натуральных числа числа и возвращает наибольшее по сумме цифр число
    """
    result_1, result_2, max_numb = 0, 0, 0
    numb_1, numb_2 = number_1, number_2
    while number_1 != 0 or number_2 != 0:
        result_1 += number_1 % 10
        result_2 += number_2 % 10
        number_1 = number_1 // 10
        number_2 = number_2 // 10
    if result_1 > result_2:
        max_numb = numb_1
    elif result_1 == result_2:
        print('Числа равны!')
        sys.exit(1)
    else:
        max_numb = numb_2
    return f'Наибольшее число: {max_numb}\n' \
           f'Сумма цифр: {max(result_1,result_2)}'


NUMBER_1, NUMBER_2 = int(input('Введите первое число: ')), int(input('Введите второе число: '))
print(max_number(NUMBER_1, NUMBER_2))
