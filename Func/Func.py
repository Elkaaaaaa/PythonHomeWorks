"""
import sys
sys.path.insert(0, 'c:\\Users\\nikkl\\OneDrive\\Рабочий стол\\GeekBrains\\Python\\HW\\Func')
import Func as f
"""


def InputNumbsInt(inputText):  # Функция ввода данных типа int
    mark = False
    while not mark:
        try:
            number = int(input(f"{inputText}"))
            mark = True
        except ValueError:
            print("Это не число типа int!")
    return number


def InputNumbsFloat(inputText):  # Функция ввода данных типа float
    mark = False
    while not mark:
        try:
            numb = float(input(f"{inputText}"))
            mark = True
        except ValueError:
            print("Это не число типа float!")
    return numb


def splitting_into_multipliers(number):  # Функция разделения числа на простые множители
    numbs = []
    k = 2
    while number != 1:
        if number % k == 0:
            numbs.append(k)
            number //= k
        else:
            k += 1
    return numbs
