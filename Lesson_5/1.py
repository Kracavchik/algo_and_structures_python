"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""


from collections import namedtuple


def company_profit():
    company_count = int(input("Введите число компаний: "))
    companies = namedtuple(
        'Company',
        'name quarter_1 quarter_2 quarter_3 quarter_4')
    profit_per_company = {}
    for i in range(company_count):
        company = companies(
            name=input(f"Введите имя {i+1}-й компании: "),
            quarter_1=int(
                input('Введите прибыль за первый квартал: ')),
            quarter_2=int(
                input('Введите прибыль за второй квартал: ')),
            quarter_3=int(
                input('Введите прибыль за третий квартал: ')),
            quarter_4=int(
                input('Введите прибыль за четвертый квартал: ')))
        profit_per_company[company.name] = (
            company.quarter_1 + company.quarter_2 + company.quarter_3 + company.quarter_4) / 4
    total_profit = 0
    for value in profit_per_company.values():
        total_profit += value
    total_profit = total_profit / company_count

    for i, j in profit_per_company.items():
        if j < total_profit:
            print(f"Прибыль компании - {i}, ниже средней.")
    for i, j in profit_per_company.items():
        if j > total_profit:
            print(f"Прибыль компании - {i}, выше средней.")


company_profit()

# Каюсь, код подсмотрел на 6-м уроке, потому что не до конца понял как работать
# с новыми коллекциями, но сейчас наконец то подразобрался.
