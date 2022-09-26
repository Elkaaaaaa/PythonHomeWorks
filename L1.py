# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.

def ex_1():
    n = int(input("Введите номер дня недели: "))
    if n in range(1,8):
        if n == 6 or n == 7:
            print("Выходной день")
        else:
            print("Будний день")
    else:    
        print("Не является днем недели")


# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def ex_2():
    xyz = ["X", "Y", "Z"]
    numbs = []
    for i in range(3):
        numbs.append(int(input(f'Введите значение {xyz[i]}:')))

    left = not (numbs[0] or numbs[1] or numbs[2])
    right = not numbs[0] and not numbs[1] and not numbs[2]

    if left == right:
        print("Выражение верно")
    else:
        print("Выражение не верно")

# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

def ex_3():
    x = int(input('Введите координату X: '))
    y = int(input('Введите координату Y: '))

    if x>0 and y>0:
        print('I четверть')
    elif x<0 and y>0:
        print('II четверть')
    elif x<0 and y<0:
        print('III четверть')
    elif x>0 and y<0:
        print('IV четверть')

# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

def ex_4():
    part = int(input('Введите номер координатной четверти: '))
    if part == 1:
        print("x:(0;+Ꝏ), y:(0;+Ꝏ)")
    elif part == 2:
        print("x:(-Ꝏ;0), y:(0;+Ꝏ)")
    elif part == 3:
        print("x:(-Ꝏ;0), y:(-Ꝏ;0)")
    elif part == 4:
        print("x:(0;+Ꝏ), y:(-Ꝏ;0)")
    else:
        print('Не является координатной четвертью')

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

def ex_5():
    def inputCoord(dot = [int], amount = int):
        xyz = ["X", "Y", "Z"]
        for i in range(amount):
            dot.append(int(input(f'Введите значение {xyz[i]}:')))
        return dot


    dotA = []
    dotB = []
    inputCoord(dotA,2)
    inputCoord(dotB,2)
    print(f"Координаты точки А:{dotA}")
    print(f"Координаты точки B:{dotB}")
    dist = round(((dotB[0]-dotA[0])*(dotB[0]-dotA[0]) + (dotB[1]-dotA[1])*(dotB[1]-dotA[1]))**(0.5), 3)
    print(f"Расстояние между точками А и B: {dist}")
    print (type (dist))

ex_1()