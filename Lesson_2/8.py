"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""


def digit_count(number: int, digit: int, count=0):
    """Принимает число и искомую цифру, возвращая количество вхожденний
       цифры в числе"""
    if len(str(number)) == 1:
        if number == digit:
            return 1
        return 0
    elif number % 10 == digit:
        count = 1 + digit_count(number//10, digit)
        return count
    count = digit_count(number//10, digit)
    return count


print(digit_count(3223, 2))
