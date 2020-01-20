"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

from random import randint
import timeit


def sum_between_index():
    numbers_lst = [randint(-100, 100) for i in range(10)]
    max_number, min_number = numbers_lst[0], numbers_lst[0]
    max_number_ind, min_number_ind = 0, 0
    numbers_sum = 0
    # print(numbers_lst)

    for i in numbers_lst:
        if i > max_number:
            max_number = i
        if i < min_number:
            min_number = i
    # print(min_number, max_number)

    if numbers_lst.index(max_number) > numbers_lst.index(min_number):
        max_number_ind = numbers_lst.index(max_number)
        min_number_ind = numbers_lst.index(min_number)
    else:
        max_number_ind = numbers_lst.index(min_number)
        min_number_ind = numbers_lst.index(max_number)

    for i in numbers_lst[min_number_ind+1:max_number_ind]:
        numbers_sum += i
    # print(numbers_sum)


# В данном скрипте производятся несколько разных операций, давайте оценим итоговую сложность в О-нотации:
# T(n) = 10(for) + 5(const) + 1(print) + 10(for) + 2(print) + 1(>) + 2(const) + от 0 до 8(for) + 1(print) = от 32 до 40 операций.
print(f'Время выполнения - {timeit.timeit("sum_between_index()", setup="from __main__ import sum_between_index", number=1000000)} миллисекунд')


def sum_between_index_2():
    numbers_lst = [randint(-100, 100) for i in range(10)]
    max_number, min_number = max(numbers_lst), min(numbers_lst)
    max_number_ind, min_number_ind = numbers_lst.index(max_number), numbers_lst.index(min_number)
    numbers_sum = sum(numbers_lst[min_number_ind+1:max_number_ind-1])
    # print(numbers_lst)
    # print(min_number, max_number)
    # print(numbers_sum)


# Давайте оценим итоговую сложность в О-нотации:
# T(n) = 10(for) + 4(const) + от 0 до 8(for) = от 14 до 22 операций.
print(f'Время выполнения - {timeit.timeit("sum_between_index_2()", setup="from __main__ import sum_between_index_2", number=1000000)} миллисекунд')
# Использование встроенных функций в сравнение с собственными, снизило количество исполняемых операций практически на
# 50%, так же сделав код более читабельным и лаконичным, однако всё же дало незначительный прирост скорости исполнения
# скрипта (~9%), в сравнение с исходным вариантом.
