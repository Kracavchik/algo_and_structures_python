"""
2*. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""

import hashlib

MY_STRING = input('Введите строку, состоящую из латинских букв: ').lower()
SUMM = set()

for i in range(len(MY_STRING)):
    for j in range(len(MY_STRING), i, -1):
        hash_string = hashlib.sha1(MY_STRING[i:j].encode('utf-8')).hexdigest()
        SUMM.add(hash_string)
print(f"В строке {MY_STRING} {len(SUMM) - 1} уникальных подстрок")
