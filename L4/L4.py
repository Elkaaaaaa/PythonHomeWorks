import random

from HW.Func.Func import InputNumbsInt, splitting_into_multipliers, InputNumbsFloat


# Вычислить число π c заданной точностью d

def ex_1():
    d = InputNumbsFloat('Введите степень точности: ')
    n = 1
    s = 0
    unit = 1
    while True:
        s = s + unit * 4 / n
        if 4 / n < d:
            break
        unit = -unit
        n = n + 2
    print(f"Вывод: {s}")


# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def ex_2():
    a = InputNumbsInt("Введите число: ")
    numbs_a = splitting_into_multipliers(a)
    print(numbs_a)


# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

def ex_3():
    dct = {}
    numbs = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]
    result = []
    for i in numbs:
        if i in dct:
            dct[i] += 1
        else:
            dct.setdefault(i, 1)
    for i in numbs:
        if dct.get(i) == 1:
            result.append(i)
    print(result)


# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

def ex_4():
    k = InputNumbsInt('Введите степень многочлена: ')
    numbs = []
    for i in range(k, 0, -1):
        numbs.append(f"{random.randint(0, 100)}*x^{i}")
    numbs.append(f"{random.randint(0, 100)}")
    with open('L4_4.txt', 'w', encoding="UTF-8") as data:
        data.write("Решение задания Номер 4: \n")
        data.write(" + ".join(numbs))
        data.write('= 0')


# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# Коэффициенты могут быть как положительными, так и отрицательными. Степени многочленов могут отличаться.

def ex_5():
    def create_poly(file_name: str):
        k = random.randint(0, 10)
        numb = []
        for c in range(k, -1, -1):
            numb.append(f"{random.randint(-100, 100)}*x^{c}")
        with open(file_name, "w", encoding="UTF-8") as data_file:
            data_file.write(" + ".join(numb))
            data_file.write('= 0')
        with open(file_name, "r", encoding="UTF-8") as data_file:
            string = data_file.readline()
        return string

    # Работа с первым многочленом в первом файле
    string_1 = create_poly('L4_5_1.txt')
    mem_1 = [e.split('*x^') for e in string_1[:len(string_1) - 3].split(" + ")]
    polynoms_1 = {}
    for i in range(len(mem_1) - 1, -1, -1):
        polynoms_1.setdefault(int(mem_1[i][1]), int(mem_1[i][0]))

    # Работа со вторым многочленом во втором файле
    string_2 = create_poly('L4_5_2.txt')
    mem_2 = [e.split('*x^') for e in string_2[:len(string_2) - 3].split(" + ")]
    polynoms_2 = {}
    for i in range(len(mem_2) - 1, -1, -1):
        polynoms_2.setdefault(int(mem_2[i][1]), int(mem_2[i][0]))

    # Работа с суммарным многочленом
    if len(mem_1) > len(mem_2):
        for i in polynoms_1:
            try:
                polynoms_1[i] += polynoms_2[i]
            except KeyError:
                continue
        result_polunoms = polynoms_1.copy()
    else:
        for i in polynoms_2:
            try:
                polynoms_2[i] += polynoms_1[i]
            except KeyError:
                continue
        result_polunoms = polynoms_2.copy()
    result = []
    for i in range(len(result_polunoms)):
        result.append(f"{result_polunoms[i]}*x^{i}")
    result.reverse()

    # Запись в третий файл
    with open("L4_5_Result.txt", "w", encoding="UTF-8") as data:
        data.write(" + ".join(result))
        data.write('= 0')
