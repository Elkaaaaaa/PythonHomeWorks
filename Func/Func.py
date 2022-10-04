"""
    import sys
    sys.path.insert(0, 'c:\\Users\\nikkl\\OneDrive\\Рабочий стол\\GeekBrains\\Python\\HW\\Func')
    import Func as f
"""



def InputNumbsInt(inputText): #Функция ввода данных типа int
    mark = False
    while not mark:
        try:
            numb = int(input(f"{inputText}"))
            mark = True
        except ValueError:
            print("Это не число типа int!")
    return numb


def InputNumbsFloat(inputText): #Функция ввода данных типа float
    mark = False
    while not mark:
        try:
            numb = float(input(f"{inputText}"))
            mark = True
        except ValueError:
            print("Это не число типа float!")
    return numb

