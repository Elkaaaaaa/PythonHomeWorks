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
def ex_2():
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
                if candy_in_game in range(a, a + 29):
                    n = candy_in_game - (a - 1)
                    candy_in_game -= n
                    print(f'\nФедя взял {n} конфет\n')
                    return candy_in_game
                else:
                    a += 29

    candy = 2021
    mode_check = InputNumbsInt('Выберете тип игры:\n0 - Игрок против Феди\n1 - Игрок против игрока\n-----> ')
    name_1 = input("Введите Ваше имя: ")
    lot = random.randint(0, 1)
    if lot == 1:
        print("Вы ходите первый ")
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
            print("Игра окончена")
        else:
            print('Такого типа игры еще нет\nЗапустите игру заново и выберете один из имеющихся типов игры:)')
    else:
        print("Вы ходите вторым")
        if mode_check == 1:
            name_2 = input("Введите имя второго игрока: ")
            while candy != 0:
                if candy != 0:
                    candy = part_of_human(name_2, candy)
                if candy != 0:
                    candy = part_of_human(name_1, candy)
            print("Игра окончена")
        elif mode_check == 0:
            while candy != 0:
                if candy != 0:
                    candy = part_of_bot(candy)
                if candy != 0:
                    candy = part_of_human(name_1, candy)
            print("Игра окончена")
        else:
            print('Такого типа игры еще нет\nЗапустите игру заново и выберете один из имеющихся типов игры:)')


# Игра в крестики-нолики
#     0  2  4
#     12 14 16
#     24 26 28

def ex_3():
    def pox(field_in_game, count_in_game):
        while True:
            k = InputNumbsInt('Ходят крестики\nВведите номер поля: ')
            k = str(k)
            if k in field_in_game:
                field_in_game = field_in_game.replace(k, "x")
                print(field_in_game)
                count_in_game += 1
                break
            else:
                print("Поле занято")
        for i in range(0, len(field_in_game), 12):
            if field_in_game[i] == field_in_game[i + 2] and field_in_game[i + 2] == field_in_game[i + 4]:
                if count_in_game % 2 != 0:
                    print("Победили крестики")
                    count_in_game = 9
        for i in range(0, 5, 2):
            if field_in_game[i] == field_in_game[i + 12] and field_in_game[i + 12] == field_in_game[i + 24]:
                if count_in_game % 2 != 0:
                    print("Победили крестики")
                    count_in_game = 9
        for i in range(0, 5, 4):
            if (field_in_game[i] == field_in_game[i + 14] and field_in_game[i + 14] == field_in_game[i + 28]) or \
                    (field_in_game[i] == field_in_game[i + 10] and field_in_game[i + 10] == field_in_game[i + 20]):
                if count_in_game % 2 != 0:
                    print("Победили крестики")
                    count_in_game = 9
        return field_in_game, count_in_game

    def poo(field_in_game, count_in_game):
        while True:
            k = InputNumbsInt('Ходят нолики\nВведите номер поля: ')
            k = str(k)
            if k in field_in_game:
                field_in_game = field_in_game.replace(k, "o")
                print(field_in_game)
                count_in_game += 1
                break
            else:
                print("Поле занято")
        for i in range(0, len(field_in_game), 12):
            if field_in_game[i] == field_in_game[i + 2] and field_in_game[i + 2] == field_in_game[i + 4]:
                if count_in_game % 2 == 0:
                    print("Победили нолики")
                    count_in_game = 9
        for i in range(0, 5, 2):
            if field_in_game[i] == field_in_game[i + 12] and field_in_game[i + 12] == field_in_game[i + 24]:
                if count_in_game % 2 == 0:
                    print("Победили нолики")
                    count_in_game = 9
        for i in range(0, 5, 4):
            if (field_in_game[i] == field_in_game[i + 14] and field_in_game[i + 14] == field_in_game[i + 28]) or \
                    (field_in_game[i] == field_in_game[i + 10] and field_in_game[i + 10] == field_in_game[i + 20]):
                if count_in_game % 2 == 0:
                    print("Победили нолики")
                    count_in_game = 9
        return field_in_game, count_in_game

    field = "1|2|3\n-----\n4|5|6\n-----\n7|8|9"
    print(field)
    count = 0
    while count != 9:
        if count % 2 == 0:
            field, count = pox(field, count)
        else:
            field, count = poo(field, count)

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
