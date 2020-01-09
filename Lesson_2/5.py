"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""

import sys


def ascii_char(start, stop, count=1, result=''):
    """Принимает два числовых значение - начала и конца последовательности.
       Выодит список ASCII символов между ними в формате - код-символ
       """
    if start == stop:
        print(f'ASCII:{stop} - Символ: {chr(stop)} ')
        sys.exit(0)
    while count < 10:
        result = result + f'ASCII:{start} - Символ: {chr(start)}' + ' '
        ascii_char(start + 1, stop, count + 1, result)
    print(result)
    ascii_char(start + 1, stop, 1)


ascii_char(32, 127)
