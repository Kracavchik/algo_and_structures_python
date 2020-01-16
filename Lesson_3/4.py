"""# 4.	Определить, какое число в массиве встречается чаще всего."""


NUMBERS_LST = [int(i)
               for i in input("Введите список чисел через пробел:\n").split(' ')]
print(NUMBERS_LST)
NUMBERS_CNT = {}
for i in NUMBERS_LST:
    if i in NUMBERS_CNT:
        NUMBERS_CNT[i] += 1
    elif i not in NUMBERS_CNT:
        NUMBERS_CNT[i] = 1
print(NUMBERS_CNT)
