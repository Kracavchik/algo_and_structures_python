"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""

import sys
import random
import time
import memory_profiler
from memory_profiler import profile


# Lesson_1_4
@profile
def first_function():
    t_p = time.process_time()
    m_p = memory_profiler.memory_usage()
    int_start = 1
    int_stop = 1000000
    print(f'Случайное число: {random.randint(int_start, int_stop)}')

    float_start = 1
    float_stop = 1000000
    print(
        f'Случайное вещественное число: {random.random() * (float_stop - float_start) + float_start}')

    char_start = 'a'
    char_stop = 'b'
    print(
        f'Случаный символ: {chr(random.randint(ord(char_start), ord(char_stop)))}')

    print(f'Выполнение заняло {t_p} сек и {m_p[0]} Мб')


'''
Windows 10 x64 Python 3.8
Время исполнения скрипта(не считая profile) ~0.1 сек, занимаемое количество памяти менее 0.0 Мб.
'''


# Lesson_2_3
def second_function():
    t_p = time.process_time()
    m_p = memory_profiler.memory_usage()

    @profile
    def recursion(number: int):
        """Принимает число и возвращает его цифры в обратном порядке"""
        answer = ''
        if len(str(number)) == 1:
            answer += str(number)
            return answer
        answer = (answer + str(number % 10)) + str(recursion(number // 10))
        return answer

    while True:
        a = random.randint(1, 100)
        try:
            a = int(a)
            print(recursion(a))
            print(f'Выполнение заняло {t_p} сек и {m_p[0]} Мб')
            sys.exit(1)
        except ValueError:
            print('Это не число!')


'''
Windows 10 x64 Python 3.8
Время исполнения скрипта(не считая profile) ~0.1 сек, занимаемое количество памяти менее 0.0 Мб.
'''


# Lesson_3_8
@profile
def third_function():
    t_p = time.process_time()
    m_p = memory_profiler.memory_usage()
    matrix = []
    for i in range(4):
        line = []
        a = 4
        for j in range(4):
            line.append(int(random.randint(0, 10)))
            a -= 1
        line.append(sum(line))
        matrix.append(line)
    for i in matrix:
        print(f'{i}')
    print(f'Выполнение заняло {t_p} сек и {m_p[0]} Мб')


'''
Windows 10 x64 Python 3.8
Время исполнения скрипта(не считая profile) ~0.1 сек, занимаемое количество памяти менее 0.0 Мб.
'''

# first_function()
# second_function()
third_function()
