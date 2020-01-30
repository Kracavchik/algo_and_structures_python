"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""


import random
import timeit


def bubble_sort(sort_lst):
    """Сортирует элементы списка от большего к меньшему"""
    for i in range(len(sort_lst)):
        for j in range(len(sort_lst) - 1):
            if sort_lst[j] < sort_lst[j + 1]:
                sort_lst[j], sort_lst[j + 1] = sort_lst[j + 1], sort_lst[j]
    print(f"Отсортированный массив - {sort_lst}")


def bubble_sort_2(sort_lst):
    """Доработанная версия, с условием прерывания перебора"""
    for i in range(len(sort_lst)):
        stop_sort = True
        for j in range(len(sort_lst) - 1):
            if sort_lst[j] < sort_lst[j + 1]:
                sort_lst[j], sort_lst[j + 1] = sort_lst[j + 1], sort_lst[j]
                stop_sort = False
        if stop_sort:
            break
    print(sort_lst)


sort_lst = [random.randint(-100, 100) for i in range(10)]

print(f"Исходный массив - {sort_lst}")
bubble_sort(sort_lst)

# print(timeit.timeit("bubble_sort(sort_lst)", setup="from __main__ import bubble_sort, sort_lst", number=1000))
# print(timeit.timeit("bubble_sort_2(sort_lst)", setup="from __main__ import bubble_sort_2, sort_lst", number=1000))

# Добавление условия прервывания перебора массива при отстутствие перестановок позволило
# ускорить работа скрипта примерно в 100 раз с 1 сек. до 0.01 при кол-ве элементов 100,
# при значение элементов в 1000 результат примерно соответственный.
