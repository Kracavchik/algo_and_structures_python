"""
2.	Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив
надо заполнить значениями 1, 4, 5, 6
(или 0, 3, 4, 5 - если индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
"""


from random import randint


NUMBERS_LST = [randint(1, 100) for i in range(10)]
INDEX_LST = []

for i in NUMBERS_LST:
    if i % 2 == 0:
        INDEX_LST.append(NUMBERS_LST.index(i))

print(f'{NUMBERS_LST}\n '
      f'{INDEX_LST}')
