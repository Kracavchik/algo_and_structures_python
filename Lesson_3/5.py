"""5.	В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию (индекс) в массиве."""


from random import randint


NUMBERS_LST = [randint(-100, 100) for i in range(10)]
MINUS_NUMBERS = [i for i in NUMBERS_LST if i < 0]
MAX_MINUS_NUMBER = MINUS_NUMBERS[0]

for i in MINUS_NUMBERS:
    if i > MAX_MINUS_NUMBER:
        MAX_MINUS_NUMBER = i

print(f'Index {NUMBERS_LST.index(MAX_MINUS_NUMBER)}\n'
      f'Number {MAX_MINUS_NUMBER}')
