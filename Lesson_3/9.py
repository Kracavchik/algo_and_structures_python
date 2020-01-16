""" 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы."""


from random import randint

M = 10
N = 5
MATRIX = []
for i in range(N):
    LINE = []
    for j in range(M):
        LINE.append(randint(1, 100))
    MATRIX.append(LINE)

for i in MATRIX:
    print(f'{i}')
print()

MIN_NUMBERS = []
for i in range(M):
    s = []
    for j in range(N):
        a = MATRIX[j][i]
        s.append(a)
    print(s)
    MIN_NUMBERS.append(min(s))

print(f'\n{MIN_NUMBERS}')
print(f'\nМинимальный элемент: {max(MIN_NUMBERS)}')
