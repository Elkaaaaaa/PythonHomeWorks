from HW.Func.Func import input_numbs_int


# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

def ex_1():
    numbs = [2, 3, 5, 9, 3]
    sum_ = 0
    for i in range(1, len(numbs), 2):
        sum_ += numbs[i]
    print(numbs, "----->", sum_)


# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def ex_2():
    numbs = [2, 3, 5, 6]
    if len(numbs) % 2 == 0:
        length = len(numbs) // 2
    else:
        length = len(numbs) // 2 + 1
    print(numbs, "----->", [numbs[i] * numbs[-i - 1] for i in range(length)])


# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

def ex_3():
    max_ = 0
    min_ = 1
    numbs = [1.1, 1.2, 3.1, 5, 10.01]
    for i in range(len(numbs)):
        while numbs[i] >= 1:
            numbs[i] = round(numbs[i] - 1, 3)
        if numbs[i] > max_:
            max_ = numbs[i]
        if numbs[i] < min_:
            if numbs[i] != 0:
                min_ = numbs[i]
    print(max_ - min_)


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def ex_4():
    number = input_numbs_int("Введите десятичное число: ")
    i = 0
    result = 0
    print(number, "--->")
    while number > 0:
        result += number % 2 * 10 ** i
        i += 1
        number //= 2
    print("--->", result)


# Задайте число.
# Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def ex_5():
    k = input_numbs_int("Введите k: ")
    fib = [0, 1]
    for i in range(2, k + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    result_fib = [fib[i] * (-1) ** (i + 1) for i in range(1, k + 1)]
    result_fib.reverse()
    result_fib.extend(fib)
    print(f"Для k = {k} ряд чисел фибоначи с отрицательными индексами принимает вид: {result_fib}")
