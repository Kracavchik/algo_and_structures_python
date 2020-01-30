"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""

import random


def quick_sort(orig_list):
    if len(orig_list) <= 1:
        return orig_list
    else:
        q = random.choice(orig_list)
        L = []
        M = []
        R = []
        for elem in orig_list:
            if elem < q:
                L.append(elem)
            elif elem > q:
                R.append(elem)
            else:
                M.append(elem)
        return quick_sort(L) + M + quick_sort(R)


def lst_median(list):
    median = 0
    if len(list) % 2:
        median = list[len(list)//2]
    else:
        median = list[len(list)//2 + 1]
    return median


numbers_lst = [random.randint(-100, 100) for i in range(2*random.randint(1, 100) + 1)]
sorted_lst = (quick_sort(numbers_lst))

print(f"Начальный массив - {numbers_lst}\n")
print(f"Отсортированный массив - {sorted_lst}\n")
print(f"Медиана - {lst_median(sorted_lst)}")
