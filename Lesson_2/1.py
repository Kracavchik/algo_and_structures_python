"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""


import sys


def first_number_ask():
    """ Запрашивает первое число и преобразует в тип float."""
    return float(input("Введите первое число: \n"))


def second_number_ask():
    """Запрашивает второе число и преобразует в тип float."""
    return float(input("Введите второе число: \n"))


def addition(number_one, number_two):
    """ Принимает два числа, осуществляет сложение и выводит результат."""
    print(f'Ответ: {number_one + number_two}\n')


def subtraction(number_one, number_two):
    """ Принимает два числа, осуществляет вычитание и выводит результат."""
    print(f'Ответ: {number_one - number_two}\n')


def multiplication(number_one, number_two):
    """ Принимает два числа, осуществляет умножение и выводит результат."""
    print(f'Ответ: {number_one * number_two}\n')


def division(number_one, number_two):
    """ Принимает два числа, осуществляет деление и выводит результат."""
    if number_one != 0 and number_two != 0:
        print(f'Ответ: {number_one / number_two}\n')
    else:
        print('На ноль делить нельзя!\n')


while True:
    ANSWER = input("Выберите тип операции: \n"
                   "Сложение - + \n"
                   "Вычитание - - \n"
                   "Умножение - *\n"
                   "Деление - /\n"                 
                   "Выход - 0\n"
                   " \n")
    if ANSWER == '+':
        addition(first_number_ask(), second_number_ask())
    elif ANSWER == '-':
        subtraction(first_number_ask(), second_number_ask())
    elif ANSWER == '*':
        multiplication(first_number_ask(), second_number_ask())
    elif ANSWER == '/':
        division(first_number_ask(), second_number_ask())
    elif ANSWER == '0':
        print('До свидания!')
        sys.exit()
    else:
        print('Такой операции нет.\n'
              'Выберите операцию из списка'
              ' \n')
