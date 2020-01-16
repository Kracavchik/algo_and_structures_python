"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""


from random import randint


NUMBERS_LST = [randint(-100, 100) for i in range(10)]
MAX_NUMBER, MIN_NUMBER = NUMBERS_LST[0], NUMBERS_LST[0]
MAX_NUMBER_IND, MIN_NUMBER_IND = 0, 0
NUMBERS_SUM = 0
print(NUMBERS_LST)

for i in NUMBERS_LST:
    if i > MAX_NUMBER:
        MAX_NUMBER = i
    if i < MIN_NUMBER:
        MIN_NUMBER = i
print(MIN_NUMBER, MAX_NUMBER)

if NUMBERS_LST.index(MAX_NUMBER) > NUMBERS_LST.index(MIN_NUMBER):
    MAX_NUMBER_IND = NUMBERS_LST.index(MAX_NUMBER)
    MIN_NUMBER_IND = NUMBERS_LST.index(MIN_NUMBER)
else:
    MAX_NUMBER_IND = NUMBERS_LST.index(MIN_NUMBER)
    MIN_NUMBER_IND = NUMBERS_LST.index(MAX_NUMBER)

for i in NUMBERS_LST[MIN_NUMBER_IND+1:MAX_NUMBER_IND]:
    NUMBERS_SUM += i
print(NUMBERS_SUM)
