# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь
import sys

def product_and_sum(number: int):
    print(f'Сумма: {(number // 100) + ((number % 100) // 10) + (number % 10)}')
    print(f'Произведение: {(number // 100) * ((number % 100) // 10) * (number % 10)}')


a = input('Введите трехзначное число: ')
try:
    int(a)
except (ValueError, TypeError):
    print('Неверное значение. Введите трехзначное число')
    sys.exit()
else:
    product_and_sum((int(a)))
