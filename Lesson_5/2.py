"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""


import collections


def hex_val(num):
    hex_v = 0
    for i in range(len(num)):
        hex_v += int(num[i], 16) * (16 ** (len(num) - i - 1))
    return hex_v


hex_numbers = collections.defaultdict(list)
hex_numbers[1] = list(input("Введите первое число: "))
hex_numbers[2] = list(input("Введите второе число: "))

hex_sum = str(hex(hex_val(hex_numbers[1]) + hex_val(hex_numbers[2])))[2:]
hex_multiple = str(hex(hex_val(hex_numbers[1]) * hex_val(hex_numbers[2])))[2:]
hex_numbers[hex_sum] = list(hex_sum)
hex_numbers[hex_multiple] = list(hex_multiple)

print(f"Сумма чисел {hex_numbers[hex_sum]}, Произведение {hex_numbers[hex_multiple]}")
