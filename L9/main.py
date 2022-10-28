import types

from telebot import *

with open("Bot Token.txt", "r", encoding="utf-8") as file:
    token = file.read()
bot = TeleBot(f'{token}')

main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
key1 = types.KeyboardButton('Крестики-Нолики')
key2 = types.KeyboardButton('Телефонный справочник')
key3 = types.KeyboardButton('Калькулятор')
main_menu.add(key1)
# main_menu.add(key2)
main_menu.add(key3)
global count
global game_menu
global keyboard_operation
global calc_keyboard
global field
global field_button


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


def calc(operation):
    def minus(lst):
        if lst[0] is None:
            return f"neg_{lst[1]}"
        else:
            for c in range(0, 2):
                if "neg" in str(lst[c]):
                    numb = list(filter(lambda e: "neg" not in e, lst[c].split("_")))
                    num = "-"
                    for i in range(len(numb)):
                        num += str(numb[i])
                    lst[c] = int(num)
                    if int(int(lst[0]) - int(lst[1])) < 0:
                        return f"neg_{abs(int(lst[0] - lst[1]))}"
                    else:
                        return int(lst[0] - lst[1])

    def multi(lst):
        for c in range(0, 2):
            if "neg" in str(lst[c]):
                numb = list(filter(lambda e: "neg" not in e, lst[c].split("_")))
                num = "-"
                for i in range(len(numb)):
                    num += str(numb[i])
                lst[c] = int(num)
        return lst[0] * lst[1]

    def divide(lst):
        for c in range(0, 2):
            if "neg" in str(lst[c]):
                numb = list(filter(lambda e: "neg" not in e, lst[c].split("_")))
                num = "-"
                for i in range(len(numb)):
                    num += str(numb[i])
                lst[c] = int(num)
        return lst[0] / lst[1]

    def count_from_string(operation_in_calculation):
        if "(" in operation_in_calculation:
            bk1 = operation_in_calculation.rindex("(")
            bk2 = operation_in_calculation.index(")", bk1)
            return count_from_string(
                operation_in_calculation[:bk1] + str(
                    count_from_string(operation_in_calculation[bk1 + 1:bk2])) + operation_in_calculation[bk2 + 1:])
        if operation_in_calculation.isdigit():
            return int(operation_in_calculation)
        if "-" in operation_in_calculation:
            return minus([count_from_string(item) for item in operation_in_calculation.split("-", 1)])
        if "+" in operation_in_calculation:
            return sum([count_from_string(item) for item in operation_in_calculation.split("+", 1)])
        if "/" in operation_in_calculation:
            return divide([count_from_string(item) for item in operation_in_calculation.split("/", 1)])
        if "*" in operation_in_calculation:
            return multi([count_from_string(item) for item in operation_in_calculation.split("*", 1)])
        if "neg" in operation_in_calculation:
            return operation_in_calculation

    return count_from_string(operation)


def calc_i(operation):
    def minus(lst):
        return lst[0] - lst[1]

    def multi(lst):
        return lst[0] * lst[1]

    def divide(lst):
        return lst[0] / lst[1]

    def count_from_string(operation_in_calculation):
        if "(" in operation_in_calculation:
            bk1 = operation_in_calculation.rindex("(")
            bk2 = operation_in_calculation.index(")", bk1)
            print(bk1, bk2)
            return count_from_string(
                operation_in_calculation[:bk1] + str(
                    count_from_string(operation_in_calculation[bk1 + 1:bk2])) + operation_in_calculation[bk2 + 1:])
        if operation_in_calculation.isdigit():
            return int(operation_in_calculation)
        if "-" in operation_in_calculation:
            return minus([count_from_string(item) for item in operation_in_calculation.split("-", 1)])
        if "+" in operation_in_calculation:
            return sum([count_from_string(item) for item in operation_in_calculation.split("+", 1)])
        if "/" in operation_in_calculation:
            return divide([count_from_string(item) for item in operation_in_calculation.split("/", 1)])
        if "*" in operation_in_calculation:
            return multi([count_from_string(item) for item in operation_in_calculation.split("*", 1)])

    return count_from_string(operation)


@bot.message_handler(commands=['start'])
def inline_key(msg):
    bot.send_message(chat_id=msg.chat.id, text='Добро пожаловть!\nВыберете действие из меню', reply_markup=main_menu)


@bot.message_handler(content_types=['text'])
def xo(msg: types.Message):
    if msg.text == 'Калькулятор':
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
        calc_keyboard.add(but_plus, but_minus, but_del)
        calc_keyboard.add(but_multy, but_divide, but_del_all)
        calc_keyboard.add(but_l_s, but_0, but_r_s)
        calc_keyboard.add(but_7, but_8, but_9)
        calc_keyboard.add(but_4, but_5, but_6)
        calc_keyboard.add(but_1, but_2, but_3)
        calc_keyboard.add(but_result)
        calc_keyboard.add(but_close)
        bot.send_message(chat_id=msg.chat.id,
                         text="Вас приветствует справка по кальлкулятору\n"
                              "\nДля запуска модуля вычислений введите\n"
                              " 'calc' \n"
                              "перед выражением или воспользуйтесь встроенной клавиатурой", reply_markup=calc_keyboard)
        keyboard_operation = ""
    if 'calc' in msg.text.lower():
        msg.text = msg.text.lower().replace(" ", "")
        msg.text = msg.text.replace("calc", "calc ")
        result = list(filter(lambda e: 'calc' not in e, msg.text.split()))
        text = ""
        for i in range(len(result)):
            text += str(result[i])
        if "i" not in text:
            try:
                res_of_calc = calc(text)
                bot.send_message(chat_id=msg.chat.id, text=f"Результат вычисления: {res_of_calc}")
            except ValueError:
                bot.send_message(chat_id=msg.chat.id, text=f"Выражение некорректо, я не могу его посчитать\n"
                                                           f"Убедитесь, что в выражении нет ничего лишнего")
        else:
            bot.send_message(chat_id=msg.chat.id, text=f"Результат вычисления: {text}")

    global game_menu
    if msg.text == 'Крестики-Нолики':
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
        if call.message:
            if call.data == "exit":
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
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text=f"Ваш результат:{calc(keyboard_operation)}")
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
            if call.data == "butClose":
                keyboard_operation = ""
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text="Надеюсь, что помог:D")


bot.infinity_polling()
