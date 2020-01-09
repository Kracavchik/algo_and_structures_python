"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""
import sys


def recursion(number: int):
    """Принимает число и возвращает его цифры в обратном порядке"""
    answer = ''
    if len(str(number)) == 1:
        answer += str(number)
        return answer
    answer = (answer + str(number % 10)) + str(recursion(number // 10))
    return answer


while True:
    A = input('Введите число: ')
    try:
        A = int(A)
        print(recursion(A))
        sys.exit(1)
    except ValueError:
        print('Это не число!')
