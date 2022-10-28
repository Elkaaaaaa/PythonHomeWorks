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
        if lst[0] is None:
            return f"neg_{lst[1]}"
        elif int(lst[0] - lst[1]) < 0:
            return f"neg_{abs(int(lst[0] - lst[1]))}"

    def multi(lst):
        for c in range(0, 2):
            if "neg" in str(lst[c]):
                numb = list(filter(lambda e: "neg" not in e, lst[c].split("_")))
                num = "-"
                for i in range(len(numb)):
                    num += str(numb[i])
                lst[c] = int(num)
        return lst[0] * lst[1]

    def divide(lst):
        for c in range(0, 2):
            if "neg" in str(lst[c]):
                numb = list(filter(lambda e: "neg" not in e, lst[c].split("_")))
                num = "-"
                for i in range(len(numb)):
                    num += str(numb[i])
                lst[c] = int(num)
        return lst[0] / lst[1]

    def count_from_string(operation_in_calculation):
        if "(" in operation_in_calculation:
            bk1 = operation_in_calculation.rindex("(")
            bk2 = operation_in_calculation.index(")", bk1)
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
        if "neg" in operation_in_calculation:
            return operation_in_calculation
    return count_from_string(operation)


# "(5-2)*((10-3)*(10-7))"
print(calc("2*(45-47)"))
# lst = ["2", "neg_6"]
# for c in range(0, 2):
#     if "neg" in lst[c]:
#         numb = list(filter(lambda e: "neg" not in e, lst[c].split("_")))
#         num = "-"
#         for i in range(len(numb)):
#             num += str(numb[i])
#         print(num)
#         print(numb)
#         lst[c] = int(num)
# print(lst)
# print(int(lst[0]) * lst[1])
