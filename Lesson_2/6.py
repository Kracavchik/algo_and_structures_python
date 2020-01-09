"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""
from random import randint
import sys


def guess_number():
    """Возвращает случайное число в диапазоне от 0 до 100"""
    return randint(0, 100)


GUESSED_NUMBER = guess_number()
ATTEMPTS = 10
print('Угадайте число от 0 до 100!\n')
while ATTEMPTS != 0:
    ATTEMPTS -= 1
    try:
        ANSWER = int(input("Введите число: "))
        if ANSWER == GUESSED_NUMBER:
            print("Правильно!")
            sys.exit(0)
        elif ANSWER > GUESSED_NUMBER:
            print('Вы ввели слишком большое число!\n'
                  f'У вас осталось {ATTEMPTS} попыток ')
        else:
            print(f'Вы ввели слишком маленькое число!\n'
                  f'У вас осталось {ATTEMPTS} попыток ')
    except ValueError:
        print('Это не число!')
print('Вы проиграли!'
      f'Правильный ответ: {guess_number()}')
