"""3.В массиве случайных целых чисел поменять местами минимальный
и максимальный элементы."""


from random import randint
from math import inf


def number_swap(number_lst):
    """Принимает список случайных чисел, меняет местами максимальный и
    минимальный элементы"""
    min_numb, max_numb = +inf, -inf
    min_numb_ind, max_numb_ind = 0, 0
    for i in number_lst:
        if i > max_numb:
            max_numb = i
            max_numb_ind = number_lst.index(i)
    for i in number_lst:
        if i < min_numb:
            min_numb = i
            min_numb_ind = number_lst.index(i)
    number_lst[max_numb_ind], number_lst[min_numb_ind] = \
        number_lst[min_numb_ind], number_lst[max_numb_ind]
    print(number_lst)


NUMBERS_LST = [randint(1, 100) for i in range(10)]
print(NUMBERS_LST)

number_swap(NUMBERS_LST)
