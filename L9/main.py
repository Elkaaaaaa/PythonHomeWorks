from telebot import *

with open("Bot Token.txt", "r", encoding="utf-8") as file:
    token = file.read()
bot = TeleBot(f'{token}')

main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
key1 = types.KeyboardButton('Крестики-Нолики')
key2 = types.KeyboardButton('Телефонная книжка')
key3 = types.KeyboardButton('/start')
main_menu.add(key1, key2, key3)
global game_menu


def revers(c):
    return not c


@bot.message_handler(commands=['start'])
def inline_key(msg):
    bot.send_message(msg.chat.id, 'Добро пожаловть в моего первого бота!', reply_markup=main_menu)


@bot.message_handler(content_types=['text'])
def xo(msg: types.Message):
    if msg.text == 'Крестики-Нолики':
        global game_menu
        bot.send_message(chat_id=msg.from_user.id, text="Добро пожаловть в игру Крестики-Нолики!")
        field = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        field_button = ["*", "*", "*", "*", "*", "*", "*", "*", "*"]
        game_menu = types.InlineKeyboardMarkup(row_width=3)
        for i in range(len(field_button)):
            field_button[i] = types.InlineKeyboardButton(text="*", callback_data=f"{i + 1}")
        for i in range(0, 9, 3):
            game_menu.add(field_button[i], field_button[i + 1], field_button[i + 2])
        new_game = types.InlineKeyboardButton(text="Выход", callback_data="exit")
        game_menu.add(new_game)
        bot.send_message(chat_id=msg.chat.id, text='Игровое поле:', reply_markup=game_menu)
    else:
        bot.send_message(chat_id=msg.chat.id, text='Главное меню', reply_markup=main_menu)

    @bot.callback_query_handler(func=lambda call: True)
    def callback_xo(call):
        if call.message:
            if call.data == "exit":
                bot.send_message(msg.chat.id, 'Добро пожаловть в моего первого бота!', reply_markup=main_menu)
            else:
                for k in range(len(field)):
                    if call.data == f"{k + 1}" and call.data in field:
                        field[k] = 'X'
                        if is_win(field, "X"):
                            for v in range(len(field)):
                                field[v] = f"{v + 1}"
                                field_button[v] = types.InlineKeyboardButton(text="*", callback_data=f"{v + 1}")
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                                  text=f'ВЫ ВЫИГРАЛИ')
                            return
                        else:
                            while True:
                                c = random.randint(1, 10)
                                if str(c) in field:
                                    field_button[c - 1] = types.InlineKeyboardButton(text="O",
                                                                                     callback_data=f"{c}")
                                    field[c - 1] = 'O'
                                    break
                            if is_win(field, 'O'):
                                for v in range(len(field)):
                                    field[v] = f"{v + 1}"
                                    field_button[v] = types.InlineKeyboardButton(text="*", callback_data=f"{v + 1}")
                                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                                      text=f'Бот ВЫИГРАЛ\n{field}\n{field_button}')
                                return
                            new_field(field_button, k, call)


def new_field(field_button, k, call):
    game_menu_call_back = types.InlineKeyboardMarkup(row_width=3)
    field_button[k] = types.InlineKeyboardButton(text="X", callback_data=f"{k}")
    for j in range(0, 9, 3):
        game_menu_call_back.add(field_button[j], field_button[j + 1], field_button[j + 2])
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


bot.infinity_polling()
