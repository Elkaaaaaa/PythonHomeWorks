# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def ex_1():
    def InputNumbs(inputText):
        mark = False
        while not mark:
            try:
                numb = float(input(f"{inputText}"))
                mark = True
            except ValueError:
                print("Это не число!")
        return numb

    def sumNums(numb):
        sum_ = 0
        for i in str(numb):
            if i != ".":
                sum_ += int(i)
        return sum_

    a = InputNumbs("Введите число: ")
    sum_ = sumNums(a)
    print(sum_)

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def ex_2():
    def InputNumbs(inputText):
        mark = False
        while not mark:
            try:
                numb = int(input(f"{inputText}"))
                mark = True
            except ValueError:
                print("Это не число!")
        return numb

    N = InputNumbs("Введите чисто N: ")
    prod_ = 1
    prods = []
    for i in range(N):
        prod_ *= i+1
        prods.append(prod_)
    print(f"Произведение число от 1 до {N}: {prods}")

# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
# округлённую до трёх знаков после точки.

def ex_3():
    def InputNumbs(inputText):
        mark = False
        while not mark:
            try:
                numb = int(input(f"{inputText}"))
                mark = True
            except ValueError:
                print("Это не число!")
        return numb

    n = InputNumbs("Введите число n: ")
    numbs = []
    sum_ = 0
    for i in range(n):
        numbs.append((1+1/(i+1))**(i+1))
    for i in range(n):
        sum_ += round(numbs[i], 3)
    print(sum_)

# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.
# Значения N, a и b вводит пользователь с клавиатуры.

def ex_4():
    import random
    numbs = []
    N = int(input("Введите N: "))
    for i in range(N):
        numbs.append(random.randint(-N, N))
    print(numbs)
    a = int(input("Введите номер первого элемента: "))
    b = int(input("Введите номер второго эелемента: "))

    result = numbs[a]*numbs[b]
    print(result)

# Реализуйте алгоритм перемешивания списка.

def ex_5():
    def shafleList(myList):
        import random
        for i in range(len(myList)):
            j = random.randint(0, i)
            myList[i], myList[j] = myList[j], myList[i]


    def inputList(myList):
        import random
        for i in range(random.randint(3, 10)):
            myList.append(random.randint(0, 10))    


    myList = []
    inputList(myList)
    print(f"Исходный список: {myList}")
    shafleList(myList)
    print(f"список после перемешивания: {myList}")