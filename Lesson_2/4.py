"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""


def list_sum(list_len: int):
    """Принимает параметр длины последовательности и возвращает сумму
       его n - элеметнов
    """
    result, next_number = 1, 1
    while list_len != 1:
        next_number = -(next_number/2)
        result = result + next_number
        list_len -= 1
    return result


print(list_sum(3))
