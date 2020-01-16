"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""


from random import randint


NUMBERS_LST = [randint(-100, 100) for i in range(10)]
print(NUMBERS_LST)
for i in range(len(NUMBERS_LST)-1):
    for j in range(len(NUMBERS_LST)-i-1):
        if NUMBERS_LST[j] > NUMBERS_LST[j+1]:
            NUMBERS_LST[j], NUMBERS_LST[j+1] = NUMBERS_LST[j+1], NUMBERS_LST[j]
print(NUMBERS_LST[0:2])
