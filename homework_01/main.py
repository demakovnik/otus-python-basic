"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [number ** 2 for number in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number):
    if number == 0 or number == 1:
        return False
    k = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            k = k + 1
    if k <= 0:
        return True
    return False


def filter_numbers(numbers_list: list, option: str):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if option == ODD:
        return [number for number in numbers_list if number % 2]
    elif option == EVEN:
        return [number for number in numbers_list if not number % 2]
    elif option == PRIME:
        return list(filter(is_prime, numbers_list))

    return None
