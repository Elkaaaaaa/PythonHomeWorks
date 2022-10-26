"""
import sys
sys.path.insert(0, 'c:\\Users\\nikkl\\OneDrive\\Рабочий стол\\GeekBrains\\Python\\HW\\Func')
import Func as f
"""


def input_numbs_int(input_text):  # Функция ввода данных типа int
    while True:
        try:
            return int(input(f"{input_text}"))
        except ValueError:
            print("Введите корректное число")


def input_numbs_float(input_text):  # Функция ввода данных типа float
    while True:
        try:
            return float(input(f"{input_text}"))
        except ValueError:
            print("Это не число типа float!")


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


def calc(operation):
    def minus(lst):
        return lst[0] - lst[1]

    def multi(lst):
        return lst[0] * lst[1]

    def divide(lst):
        return lst[0] / lst[1]

    def count_from_string(operation_in_calculation):
        if "(" in operation_in_calculation:
            bk1 = operation_in_calculation.rindex("(")
            bk2 = operation_in_calculation.index(")", bk1)
            print(bk1, bk2)
            return count_from_string(
                operation_in_calculation[:bk1] + str(
                    count_from_string(operation_in_calculation[bk1 + 1:bk2])) + operation_in_calculation[bk2 + 1:])
        if operation_in_calculation.isdigit():
            return int(operation_in_calculation)
        if "-" in operation_in_calculation:
            return minus([count_from_string(item) for item in operation_in_calculation.split("-", 1)])
        if "+" in operation_in_calculation:
            return sum([count_from_string(item) for item in operation_in_calculation.split("+", 1)])
        if "/" in operation_in_calculation:
            return divide([count_from_string(item) for item in operation_in_calculation.split("/", 1)])
        if "*" in operation_in_calculation:
            return multi([count_from_string(item) for item in operation_in_calculation.split("*", 1)])

    count_from_string(operation)
