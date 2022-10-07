import random

from HW.Func.Func import InputNumbsInt


# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def ex_1():
    with open("Lesson5_1_1", "w", encoding="UTF-8") as data_file:
        data_file.writelines("мне просто мне нравится\nмне очень прям мне\nмне прям мне")
    with open("Lesson5_1_1", "r", encoding="UTF-8") as data_file:
        string = data_file.readlines()
    result = []
    for i in range(len(string)):
        string[i] = string[i].split()
        result.append(list(filter(lambda e: 'мне' not in e, string[i])))
    with open("Lesson5_1_2", "w", encoding="UTF-8") as data_file:
        for i in range(len(result)):
            data_file.writelines(" ".join(result[i]) + "\n")


# Игра с конфетами


def part_of_human(name, candy_in_game):
    while True:
        print(f"\nВ мешке осталось {candy_in_game} конфет!")
        n = InputNumbsInt(f"Ход Игрока {name}\nВведите количество конфет: ")
        if n <= 28:
            if candy_in_game >= n:
                candy_in_game -= n
                break
            else:
                print('Введите число конфет, меньшее, чем осталось в мешке')
        else:
            print("Вы не можете взять больше 28 конфет")
    if candy_in_game == 0:
        print(f'\nИгрок {name} победил!!!\n')
        return candy_in_game
    return candy_in_game


def part_of_bot(candy_in_game):
    print(f"\nВ мешке осталось {candy_in_game} конфет!\nХодит Федя")
    a = 30
    if candy_in_game <= 28:
        candy_in_game -= candy_in_game
        print('Федя победил!!!')
        return candy_in_game
    elif candy_in_game == 29:
        n = random.randint(1, 28)
        candy_in_game -= n
        print(f'\nФедя взял {n} конфет\n')
        return candy_in_game
    else:
        while True:
            if candy_in_game in range(a, a+29):
                n = candy_in_game - (a - 1)
                candy_in_game -= n
                print(f'\nФедя взял {n} конфет\n')
                return candy_in_game
            else:
                a += 29


candy = 200
mode_check = InputNumbsInt('Выберете тип игры:\n0 - Игрок против бота\n1 - Игрок против игрока\n-----> ')
name_1 = input("Введите Ваше имя: ")
if mode_check == 1:
    name_2 = input("Введите имя второго игрока: ")
    while candy != 0:
        if candy != 0:
            candy = part_of_human(name_1, candy)
        if candy != 0:
            candy = part_of_human(name_2, candy)
    print("Игра окончена")
elif mode_check == 0:
    while candy != 0:
        if candy != 0:
            candy = part_of_human(name_1, candy)
        if candy != 0:
            candy = part_of_bot(candy)
else:
    print('Такого мода игры еще нет\nВыберете из имеющихся:)')
