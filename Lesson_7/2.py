"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""


import random


def merge_sort(sort_lst):
    if len(sort_lst) > 1:
        center = len(sort_lst) // 2
        left = sort_lst[:center]
        right = sort_lst[center:]

        merge_sort(left)
        merge_sort(right)

        l_idx, r_idx, idx = 0, 0, 0

        while l_idx < len(left) and r_idx < len(right):
            if left[l_idx] < right[r_idx]:
                sort_lst[idx] = left[l_idx]
                l_idx += 1
            else:
                sort_lst[idx] = right[r_idx]
                r_idx += 1
            idx += 1

        while l_idx < len(left):
            sort_lst[idx] = left[l_idx]
            l_idx += 1
            idx += 1

        while r_idx < len(right):
            sort_lst[idx] = right[r_idx]
            r_idx += 1
            idx += 1
        return sort_lst


sort_lst = [random.randint(0, 51) for i in range(10)]
print(sort_lst)
print(merge_sort(sort_lst))
