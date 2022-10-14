import random

from HW.Func.Func import InputNumbsInt


def ex_1():
    # Задача 4. Семинар 5.
    # Было
    def bring_back(result_string):
        back_list = []
        back_string = ""
        for i in range(len(result_string)):
            back_list.append(result_string[i])
        for i in range(0, len(back_list), 2):
            n = int(back_list[i])
            while n != 0:
                back_string += back_list[i + 1]
                n -= 1
        return back_string

    # Стало
    def bring_back(result_string):
        back_string = ""
        back_list = [el for el in result_string]
        for i in range(0, len(back_list), 2):
            n = int(back_list[i])
            while n != 0:
                back_string += back_list[i + 1]
                n -= 1
        return back_string


def ex_2():
    # Задача 5. Семинар 3.
    # Было
    k = InputNumbsInt("Введите k: ")
    fib = [0, 1]
    result_fib = []
    for i in range(2, k + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    for i in range(1, k + 1):
        result_fib.append(fib[i] * (-1) ** (i + 1))
    result_fib.reverse()
    result_fib.extend(fib)
    # Стало
    k = InputNumbsInt("Введите k: ")
    fib = [0, 1]
    for i in range(2, k + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    result_fib = [fib[i] * (-1) ** (i + 1) for i in range(1, k + 1)]
    result_fib.reverse()
    result_fib.extend(fib)


def ex_3():
    # Задача 3. Семинар 2.
    # Было
    n = InputNumbsInt("Введите число n: ")
    numbs = []
    sum_ = 0
    for i in range(n):
        numbs.append((1 + 1 / (i + 1)) ** (i + 1))
    for i in range(n):
        sum_ += round(numbs[i], 3)
    print(sum_)
    # Стало
    n = InputNumbsInt("Введите число n: ")
    numbs = [(1 + 1 / (i + 1)) ** (i + 1) for i in range(n)]
    sum_ = 0
    for i in range(n):
        sum_ += round(numbs[i], 3)
    print(sum_)


def ex_4():
    # Задача 4. Семинар 2.
    # Было
    n = InputNumbsInt("Введите n: ")
    numbs = []
    for i in range(n):
        numbs.append(random.randint(-n, n))
    print(numbs)
    a = int(input("Введите номер первого элемента: "))
    b = int(input("Введите номер второго эелемента: "))
    result = numbs[a] * numbs[b]
    print(result)
    # Стало
    n = InputNumbsInt("Введите n: ")
    numbs = [random.randint(-n, n) for i in range(n)]
    print(numbs)
    a = int(input("Введите номер первого элемента: "))
    b = int(input("Введите номер второго эелемента: "))
    result = numbs[a] * numbs[b]
    print(result)


def ex_5():
    # Задача 2. Семинар 3.
    # Было
    prods = []
    numbs = [2, 3, 5, 6]
    if len(numbs) % 2 == 0:
        length = len(numbs) // 2
    else:
        length = len(numbs) // 2 + 1
    for i in range(length):
        prods.append(numbs[i] * numbs[-i - 1])
    print(numbs, "----->", prods)
    # Стало
    numbs = [2, 3, 5, 6]
    if len(numbs) % 2 == 0:
        length = len(numbs) // 2
    else:
        length = len(numbs) // 2 + 1
    print(numbs, "----->", [numbs[i] * numbs[-i - 1] for i in range(length)])


def ex_6():
    # Задача 5. Семинар 2.
    # Было
    def ex_5():
        def shaffle_list(my_list_build):
            for i in range(len(my_list_build)):
                j = random.randint(0, i)
                my_list_build[i], my_list_build[j] = my_list_build[j], my_list_build[i]

        def input_list(my_list_build):
            my_list_build = []
            for i in range(random.randint(3, 10)):
                my_list_build.append(random.randint(0, 10))

        my_list = []
        input_list(my_list)
        print(f"Исходный список: {my_list}")
        shaffle_list(my_list)
        print(f"список после перемешивания: {my_list}")

    # Стало
    def ex_5():
        def shaffle_list(my_list_build):
            for i in range(len(my_list_build)):
                j = random.randint(0, i)
                my_list_build[i], my_list_build[j] = my_list_build[j], my_list_build[i]

        my_list = [random.randint(0, 10) for i in range(random.randint(3, 10))]
        print(f"Исходный список: {my_list}")
        shaffle_list(my_list)
        print(f"список после перемешивания: {my_list}")
