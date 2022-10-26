from HW.Func.Func import input_numbs_int, input_numbs_float
import random


# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def ex_1():
    def sum_nums(numb):
        sum_ = 0
        for i in str(numb):
            if i != ".":
                sum_ += int(i)
        return sum_

    a = input_numbs_float("Введите число: ")
    sum_ = sum_nums(a)
    print(sum_)


# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def ex_2():
    N = input_numbs_int("Введите чисто N: ")
    prod_ = 1
    prods = []
    for i in range(N):
        prod_ *= i + 1
        prods.append(prod_)
    print(f"Произведение число от 1 до {N}: {prods}")


# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
# округлённую до трёх знаков после точки.

def ex_3():
    n = input_numbs_int("Введите число n: ")
    numbs = [(1 + 1 / (i + 1)) ** (i + 1) for i in range(n)]
    sum_ = 0
    for i in range(n):
        sum_ += round(numbs[i], 3)
    print(sum_)


# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.
# Значения N, a и b вводит пользователь с клавиатуры.

def ex_4():
    import random
    N = input_numbs_int("Введите N: ")
    numbs = [random.randint(-N, N) for i in range(N)]
    print(numbs)
    a = int(input("Введите номер первого элемента: "))
    b = int(input("Введите номер второго эелемента: "))
    result = numbs[a] * numbs[b]
    print(result)


# Реализуйте алгоритм перемешивания списка.

def ex_5():
    def shaffle_list(my_list_build):
        for i in range(len(my_list_build)):
            j = random.randint(0, i)
            my_list_build[i], my_list_build[j] = my_list_build[j], my_list_build[i]

    my_list = [random.randint(0, 10) for i in range(random.randint(3, 10))]
    print(f"Исходный список: {my_list}")
    shaffle_list(my_list)
    print(f"список после перемешивания: {my_list}")
