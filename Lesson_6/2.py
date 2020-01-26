"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""


from pympler import asizeof


class Human:
    """Тестовый класс 1"""
    __slots__ = ('first_name', 'last_name')

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class NewHuman:
    """Тестовый класс 2"""
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


ALEXANDR = Human('Alexandr', 'Nevsky')
print(asizeof.asizeof(ALEXANDR))
VLADIMIR = NewHuman('Vladimir', 'Johnson')
print(asizeof.asizeof(VLADIMIR))
print(VLADIMIR.__dict__)

# Класс с применением слотов даёт более 50% экономию памяти,
# при невозможности добавления доп атрибутов.
