"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""


def odd_even_count(number: int):
    """Принимает число и возвращает количество его четный и нечетных цифр"""
    even, odd = 0, 0
    while number != 0:
        if (number % 10) % 2 == 0:
            even += 1
            number = number // 10
        else:
            odd += 1
            number = number // 10
    print(f'Четных: {even}\n'
          f'Нечетных: {odd}')


NUMBER = int(input('Введите число: \n'))
odd_even_count(NUMBER)
