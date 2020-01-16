""" 1.	В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9."""


NUMBERS_LST = range(2, 100)
NUMBERS_CNT = {i: 0 for i in range(2, 10)}

for i in NUMBERS_LST:
    for j in NUMBERS_CNT:
        if i % j == 0:
            NUMBERS_CNT[j] += 1

print(NUMBERS_CNT)
