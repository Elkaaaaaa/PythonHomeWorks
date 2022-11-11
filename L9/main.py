import types

from telebot import *

with open("Bot Token.txt", "r", encoding="utf-8") as file:
    token = file.read()
bot = TeleBot(f'{token}')


def log(text):
    with open("log.txt", "a", encoding="utf-8") as logfile:
        print(datetime.now(), text, file=logfile)


log(f"---> Бот запущен")
main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
key1 = types.KeyboardButton('Крестики-Нолики')
key2 = types.KeyboardButton('Телефонный справочник')
key3 = types.KeyboardButton('Калькулятор')
key4 = types.KeyboardButton('Log')
main_menu.add(key1)
# main_menu.add(key2)
main_menu.add(key3)
main_menu.add(key4)
global count
global game_menu
global field
global field_button
global keyboard_operation
global calc_keyboard


def calc(operation):
    def minus(lst):
        if lst[0] is None:
            return f"neg_{lst[1]}"
        else:
            for c in range(0, 2):
                if "neg" in str(lst[c]):
                    numb = list(filter(lambda el: "neg" not in el, lst[c].split("_")))
                    num = "-"
                    for i in range(len(numb)):
                        num += str(numb[i])
                    lst[c] = float(num)
            if float(float(lst[0]) - float(lst[1])) < 0:
                return f"neg_{abs(float(lst[0]) - float(lst[1]))}"
            else:
                return float(lst[0]) - float(lst[1])

    def multi(lst):
        for c in range(0, 2):
            if "neg" in str(lst[c]):
                numb = list(filter(lambda el: "neg" not in el, lst[c].split("_")))
                num = "-"
                for i in range(len(numb)):
                    num += str(numb[i])
                lst[c] = float(num)
        return float(lst[0]) * float(lst[1])

    def divide(lst):
        for c in range(0, 2):
            if "neg" in str(lst[c]):
                numb = list(filter(lambda el: "neg" not in el, lst[c].split("_")))
                num = "-"
                for i in range(len(numb)):
                    num += str(numb[i])
                lst[c] = float(num)
        return float(lst[0]) / float(lst[1])

    def count_from_string(operation_in_calculation):
        if "(" in operation_in_calculation:
            bk1 = operation_in_calculation.rindex("(")
            bk2 = operation_in_calculation.index(")", bk1)
            return count_from_string(
                operation_in_calculation[:bk1] + str(
                    count_from_string(operation_in_calculation[bk1 + 1:bk2])) + operation_in_calculation[bk2 + 1:])
        try:
            if isinstance(float(operation_in_calculation), float):
                return operation_in_calculation
        except ValueError:
            pass
        if "-" in operation_in_calculation:
            temp1 = operation_in_calculation.split("-", 1)
            temp = temp1[1].replace('-', '%temp%').replace('+', '-').replace('%temp%', '+')
            operation_in_calculation = temp1[0] + "-" + temp
            return minus([count_from_string(item) for item in operation_in_calculation.split("-", 1)])
        if "+" in operation_in_calculation:
            return sum([count_from_string(item) for item in operation_in_calculation.split("+", 1)])
        if "/" in operation_in_calculation:
            return divide([count_from_string(item) for item in operation_in_calculation.split("/", 1)])
        if "*" in operation_in_calculation:
            return multi([count_from_string(item) for item in operation_in_calculation.split("*", 1)])
        if "neg" in operation_in_calculation:
            return operation_in_calculation

    result = count_from_string(operation)
    if "neg" in result:
        numb_calc = list(filter(lambda el: "neg" not in el, result.split("_")))
        num_calc = "-"
        for p in range(len(numb_calc)):
            num_calc += str(numb_calc[p])
        return float(num_calc)
    else:
        return float(result)


def new_field(field_button_new_field, k, call):
    game_menu_call_back = types.InlineKeyboardMarkup(row_width=3)
    field_button_new_field[k] = types.InlineKeyboardButton(text="❌", callback_data=f"{k + 10}")
    for j in range(0, 9, 3):
        game_menu_call_back.add(field_button_new_field[j], field_button_new_field[j + 1],
                                field_button_new_field[j + 2])
    new_game_call_back = types.InlineKeyboardButton(text="Выход", callback_data="exit")
    game_menu_call_back.add(new_game_call_back)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                          text='Игровое поле',
                          reply_markup=game_menu_call_back)


def is_win(arr, who):
    if (((arr[0] == who) and (arr[4] == who) and (arr[8] == who)) or
            ((arr[2] == who) and (arr[4] == who) and (arr[6] == who)) or
            ((arr[0] == who) and (arr[1] == who) and (arr[2] == who)) or
            ((arr[3] == who) and (arr[4] == who) and (arr[5] == who)) or
            ((arr[6] == who) and (arr[7] == who) and (arr[8] == who)) or
            ((arr[0] == who) and (arr[3] == who) and (arr[6] == who)) or
            ((arr[1] == who) and (arr[4] == who) and (arr[7] == who)) or
            ((arr[2] == who) and (arr[5] == who) and (arr[8] == who))):
        return True
    return False


@bot.message_handler(commands=['start'])
def inline_key(msg):
    bot.send_message(chat_id=msg.chat.id, text='Добро пожаловть!\nВыберете действие из меню', reply_markup=main_menu)


@bot.message_handler(content_types=['text'])
def xo(msg: types.Message):
    if msg.text == 'Log':
        with open("log.txt", "rb") as logfile:
            read_file = logfile.read()
        bot.send_message(chat_id=msg.chat.id, text="Log:")
        bot.send_document(chat_id=msg.chat.id, document=read_file)
    if msg.text == 'Калькулятор':
        log("--> Запуск калькулятора")
        global keyboard_operation
        global calc_keyboard
        calc_keyboard = types.InlineKeyboardMarkup(row_width=3)
        but_1 = types.InlineKeyboardButton(text="1", callback_data="but1")
        but_2 = types.InlineKeyboardButton(text="2", callback_data="but2")
        but_3 = types.InlineKeyboardButton(text="3", callback_data="but3")
        but_4 = types.InlineKeyboardButton(text="4", callback_data="but4")
        but_5 = types.InlineKeyboardButton(text="5", callback_data="but5")
        but_6 = types.InlineKeyboardButton(text="6", callback_data="but6")
        but_7 = types.InlineKeyboardButton(text="7", callback_data="but7")
        but_8 = types.InlineKeyboardButton(text="8", callback_data="but8")
        but_9 = types.InlineKeyboardButton(text="9", callback_data="but9")
        but_0 = types.InlineKeyboardButton(text="0", callback_data="but0")
        but_j = types.InlineKeyboardButton(text="j", callback_data="butj")
        but_plus = types.InlineKeyboardButton(text="+", callback_data="but+")
        but_minus = types.InlineKeyboardButton(text="-", callback_data="but-")
        but_multy = types.InlineKeyboardButton(text="*", callback_data="but*")
        but_divide = types.InlineKeyboardButton(text="/", callback_data="but/")
        but_r_s = types.InlineKeyboardButton(text=")", callback_data="but)")
        but_l_s = types.InlineKeyboardButton(text="(", callback_data="but(")
        but_del = types.InlineKeyboardButton(text="<", callback_data="but<")
        but_del_all = types.InlineKeyboardButton(text="C", callback_data="butC")
        but_close = types.InlineKeyboardButton(text="Close", callback_data="butClose")
        but_result = types.InlineKeyboardButton(text="=", callback_data="but=")
        but_dot = types.InlineKeyboardButton(text=".", callback_data="but.")
        calc_keyboard.add(but_plus, but_minus, but_del)
        calc_keyboard.add(but_multy, but_divide, but_del_all)
        calc_keyboard.add(but_l_s, but_r_s, but_j)
        calc_keyboard.add(but_7, but_8, but_9)
        calc_keyboard.add(but_4, but_5, but_6)
        calc_keyboard.add(but_1, but_2, but_3)
        calc_keyboard.add(but_dot, but_0, but_result)
        calc_keyboard.add(but_close)
        bot.send_message(chat_id=msg.chat.id,
                         text="Вас приветствует справка по кальлкулятору\n"
                              "Воспользуйтесь встроенной клавиатурой^^", reply_markup=calc_keyboard)
        keyboard_operation = ""

    global game_menu
    if msg.text == 'Крестики-Нолики':
        log("--> Запуск игры 'Крестики-Нолики'")
        global count
        global field
        global field_button
        count = 0
        field = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        field_button = ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"]
        game_menu = types.InlineKeyboardMarkup(row_width=3)
        for i in range(len(field_button)):
            field_button[i] = types.InlineKeyboardButton(text="⬜️", callback_data=f"{i + 1}")
        for i in range(0, 9, 3):
            game_menu.add(field_button[i], field_button[i + 1], field_button[i + 2])
        new_game = types.InlineKeyboardButton(text="Выход", callback_data="exit")
        game_menu.add(new_game)
        bot.send_message(chat_id=msg.chat.id, text='Добро пожаловть в игру\nКрестики-Нолики!', reply_markup=game_menu)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    global game_menu
    global count
    global keyboard_operation

    def loger(text):
        with open("log.txt", "a", encoding="utf-8") as filelog:
            print(datetime.now(), text, file=filelog)

    if call.message:
        if call.data == "exit":
            loger("->Досрочный выход из игры")
            for v in range(len(field)):
                field[v] = f"{v + 1}"
                count = 0
                field_button[v] = types.InlineKeyboardButton(text="⬜️", callback_data=f"{v + 1}")
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='Возвращайся!')
        if call.data.isdigit() and int(call.data) in range(len(field) + 1):
            for k in range(len(field)):
                if call.data == f"{k + 1}" and call.data in field:
                    field[k] = '❌'
                    count += 1
                    if is_win(field, "❌"):
                        for o in range(len(field)):
                            if field[o].isdigit():
                                field[o] = "⬜️"
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                              text=f'ВЫ ВЫИГРАЛИ\n{field[0]} {field[1]} {field[2]}'
                                                   f'\n{field[3]} {field[4]} {field[5]}\n'
                                                   f'{field[6]} {field[7]} {field[8]}')
                        loger("->Победа пользователя")
                        count = 0
                        for v in range(len(field)):
                            field[v] = f"{v + 1}"
                            field_button[v] = types.InlineKeyboardButton(text="⬜️", callback_data=f"{v + 1}")
                        return
                    elif count == 9:
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                              text=f'Ничья!!!\n{field[0]} {field[1]} {field[2]}'
                                                   f'\n{field[3]} {field[4]} {field[5]}\n'
                                                   f'{field[6]} {field[7]} {field[8]}')
                        loger("->Ничья")
                    else:
                        while True:
                            c = random.randint(1, 10)
                            if str(c) in field:
                                field_button[c - 1] = types.InlineKeyboardButton(text="⭕️",
                                                                                 callback_data=f"{c + 10}")
                                field[c - 1] = '⭕️'
                                count += 1
                                break
                        if is_win(field, '⭕️'):
                            for o in range(len(field)):
                                if field[o].isdigit():
                                    field[o] = "⬜️"
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                                  text=f'Бот ВЫИГРАЛ\n{field[0]} {field[1]} {field[2]}'
                                                       f'\n{field[3]} {field[4]} {field[5]}\n'
                                                       f'{field[6]} {field[7]} {field[8]}')
                            loger("->Победа бота")
                            count = 0
                            for v in range(len(field)):
                                field[v] = f"{v + 1}"
                                field_button[v] = types.InlineKeyboardButton(text="⬜️", callback_data=f"{v + 1}")
                            return
                        new_field(field_button, k, call)
        if call.data == "but1":
            keyboard_operation += "1"
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text=f">>>>>>>>>>>>>>>>>> {keyboard_operation}", reply_markup=calc_keyboard)
        if call.data == "butj":
            keyboard_operation += "j"
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text=f">>>>>>>>>>>>>>>>>> {keyboard_operation}", reply_markup=calc_keyboard)
        if call.data == "but2":
            keyboard_operation += "2"
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text=f">>>>>>>>>>>>>>>>>> {keyboard_operation}", reply_markup=calc_keyboard)
        if call.data == "but3":
            keyboard_operation += "3"
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text=f">>>>>>>>>>>>>>>>>> {keyboard_operation}", reply_markup=calc_keyboard)
        if call.data == "but4":
            keyboard_operation += "4"
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text=f">>>>>>>>>>>>>>>>>> {keyboard_operation}", reply_markup=calc_keyboard)
        if call.data == "but5":
            keyboard_operation += "5"
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text=f">>>>>>>>>>>>>>>>>> {keyboard_operation}", reply_markup=calc_keyboard)
        if call.data == "but6":
            keyboard_operation += "6"
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text=f">>>>>>>>>>>>>>>>>> {keyboard_operation}", reply_markup=calc_keyboard)
        if call.data == "but7":
            keyboard_operation += "7"
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text=f">>>>>>>>>>>>>>>>>> {keyboard_operation}", reply_markup=calc_keyboard)
        if call.data == "but8":
            keyboard_operation += "8"
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text=f">>>>>>>>>>>>>>>>>> {keyboard_operation}", reply_markup=calc_keyboard)
        if call.data == "but9":
            keyboard_operation += "9"
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text=f">>>>>>>>>>>>>>>>>> {keyboard_operation}", reply_markup=calc_keyboard)
        if call.data == "but0":
            keyboard_operation += "0"
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text=f">>>>>>>>>>>>>>>>>> {keyboard_operation}", reply_markup=calc_keyboard)
        if call.data == "but+":
            keyboard_operation += "+"
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text=f">>>>>>>>>>>>>>>>>> {keyboard_operation}", reply_markup=calc_keyboard)
        if call.data == "but-":
            keyboard_operation += "-"
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text=f">>>>>>>>>>>>>>>>>> {keyboard_operation}", reply_markup=calc_keyboard)
        if call.data == "but=":
            try:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text=f"Ваш результат:{eval(keyboard_operation)}")
                loger(f"-> Пользователь ввел строку '{keyboard_operation}'"
                      f", Результат: {eval(keyboard_operation)}")
            except SyntaxError:
                loger(f"-> Пользователь ввел строку '{keyboard_operation}'"
                      f", Некорректный ввод")
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text=f"Перепроверьте строку "
                                           f">>>>>>>>>>>>>>>>>> {keyboard_operation}", reply_markup=calc_keyboard)
            except ValueError:
                loger(f"-> Пользователь ввел строку '{keyboard_operation}'"
                      f", Некорректный ввод")
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text=f"Перепроверьте строку "
                                           f">>>>>>>>>>>>>>>>>> {keyboard_operation}", reply_markup=calc_keyboard)
            except NameError:
                loger(f"-> Пользователь ввел строку '{keyboard_operation}'"
                      f", Некорректный ввод")
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text=f"Перепроверьте строку\n"
                                           f"Если у вас стоит просто 'j' замените на '1j'"
                                           f">>>>>>>>>>>>>>>>>> {keyboard_operation}", reply_markup=calc_keyboard)
        if call.data == "but*":
            keyboard_operation += "*"
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text=f">>>>>>>>>>>>>>>>>> {keyboard_operation}", reply_markup=calc_keyboard)
        if call.data == "but/":
            keyboard_operation += "/"
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text=f">>>>>>>>>>>>>>>>>> {keyboard_operation}", reply_markup=calc_keyboard)
        if call.data == "but<":
            keyboard_operation = keyboard_operation[:len(keyboard_operation) - 1]
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text=f">>>>>>>>>>>>>>>>>> {keyboard_operation}", reply_markup=calc_keyboard)
        if call.data == "but(":
            keyboard_operation += "("
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text=f">>>>>>>>>>>>>>>>>> {keyboard_operation}", reply_markup=calc_keyboard)
        if call.data == "but)":
            keyboard_operation += ")"
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text=f">>>>>>>>>>>>>>>>>> {keyboard_operation}", reply_markup=calc_keyboard)
        if call.data == "butC":
            keyboard_operation = ""
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text=f">>>>>>>>>>>>>>>>>> {keyboard_operation}", reply_markup=calc_keyboard)
        if call.data == "but.":
            keyboard_operation += "."
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text=f">>>>>>>>>>>>>>>>>> {keyboard_operation}", reply_markup=calc_keyboard)
        if call.data == "butClose":
            keyboard_operation += "."
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text="Заходи, если что)")


bot.polling()
