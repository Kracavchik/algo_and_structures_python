# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).

first = int(input('Введите первое число\n'))
second = int(input('Введите второе число\n'))
third = int(input('Введите третье число\n'))

if first == second or second == third or first == third:
    print('Введены одинаковые числа')
    exit(0)

if first > second:
    max_n = first
    min_n = second
else:
    max_n = second
    min_n = first

if third > max_n:
    max_n = third

if third < min_n:
    min_n = third

print(f'Среднее число {first + second + third - max_n - min_n}')
