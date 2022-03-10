# Телеграм-бот v.002 - бот создаёт меню, присылает собачку, и анекдот

import telebot  # pyTelegramBotAPI	4.3.1
from telebot import types

bot = telebot.TeleBot('5015391881:AAEq_NV09_lq4cPdyBUYlwBu-HtUmF6wpHI')  # Создаем экземпляр бота

# -----------------------------------------------------------------------
# Функция, обрабатывающая команду /start
def inputBot(message, text):
    a = []
    def ret(message):
        a.clear()
        a.append(message.text)
        return False

    a.clear()
    mes = bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(message, ret)
    while a == []:
        pass
    return a[0]
@bot.message_handler(commands=["start"])
def start(message, res=False):
    chat_id = message.chat.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Главное меню")
    btn2 = types.KeyboardButton("❓ Помощь")
    markup.add(btn1, btn2)

    bot.send_message(chat_id,
                     text="Привет, {0.first_name}! Я тестовый бот для курса программирования на языке ПаЙтон".format(
                         message.from_user), reply_markup=markup)


# -----------------------------------------------------------------------
# Получение сообщений от юзера
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    ms_text = message.text

    if ms_text == "Главное меню" or ms_text == "👋 Главное меню" or ms_text == "Вернуться в главное меню":  # ..........
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Развлечения")
        btn2 = types.KeyboardButton("WEB-камера")
        btn3 = types.KeyboardButton("Управление")
        btn4 = types.KeyboardButton('дз')
        btn5 = types.KeyboardButton('Даня говноед')
        back = types.KeyboardButton("Помощь")
        markup.add(btn1, btn2, btn3, btn4, btn5, back)
        bot.send_message(chat_id, text="Вы в главном меню", reply_markup=markup)

    elif ms_text == "Развлечения":  # ..................................................................................
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Прислать собаку")
        btn2 = types.KeyboardButton("Прислать анекдот")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(chat_id, text="Развлечения", reply_markup=markup)

    elif ms_text == "/dog" or ms_text == "Прислать собаку":  # .........................................................
        bot.send_message(chat_id, text="🐕")

    elif ms_text == "Прислать анекдот":  # .............................................................................
        bot.send_message(chat_id, text= "Мне можно доверять свои секреты, хотя бы потому что, я на следующий день их забуду.")

    elif ms_text == "WEB-камера":
        img2 = open('кот.jpg', 'rb')
        bot.send_photo(message.chat.id, img2)
    elif ms_text == 'Даня говноед':
        bot.send_message(chat_id, text="💩")



    elif ms_text == "Управление":  # ...................................................................................
        bot.send_message(chat_id, text="еще не готово...")

    elif ms_text == "Помощь" or ms_text == "/help":  # .................................................................
        bot.send_message(chat_id, "Автор: Арина Зорина")
        key1 = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="Напишите автору", url="https://www.instagram.com/mschelou/")
        key1.add(btn1)
        img = open('я.jpg', 'rb')
        bot.send_photo(message.chat.id, img, reply_markup=key1)
    elif ms_text == 'дз':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        p1 = types.KeyboardButton('Задание 1')
        p2 = types.KeyboardButton('Задание 2')
        p3 = types.KeyboardButton('Задание 3')
        p4 = types.KeyboardButton('Задание 4')
        p5 = types.KeyboardButton('Задание 5')
        p6 = types.KeyboardButton('Задание 6')
        p7 = types.KeyboardButton('Задание 7')
        p8 = types.KeyboardButton('Задание 8')
        p9 = types.KeyboardButton('Задание 9')
        p10 = types.KeyboardButton('Задание 10')
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, back)
        bot.send_message(chat_id, text='дз', reply_markup=markup)
    elif ms_text == 'Задание 4':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key1 = types.InlineKeyboardMarkup()
        name = inputBot(message, "Как Вас зовут?")
        while name.isnumeric() == True:
            name = inputBot(message, "Введите верное имя")
        bot.send_message(chat_id, text="Приятно познакомиться, " + name)
        age=inputBot(message, "Сколько тебе лет?")
        while age.isnumeric()==False:
            age = inputBot(message, "Введите верный возраст")
        bot.send_message(chat_id, text="Ого, тебе уже " + age +"! Выглядишь намного моложе")
    elif ms_text == 'Задание 1':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        myname = 'Арина'
        bot.send_message(chat_id, text="Привет, меня зовут " + myname)
    elif ms_text == 'Задание 2':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        myname = 'Арина'
        myage = '18'
        bot.send_message(chat_id, text="Привет, меня зовут " + myname+', мне '+myage)
    elif ms_text == 'Задание 3':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        myname = 'Арина'
        myname2=myname*5
        bot.send_message(chat_id, text="Мое имя 5 раз подряд: " + myname2)
    elif ms_text == 'Задание 5':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        how_old_are_u = int(inputBot(message, "Сколько тебе лет?"))
        if (int(how_old_are_u) > 0) and (how_old_are_u < 18):
            bot.send_message(chat_id, text="Никто не определит Ваш возраст лучше, чем продавщица сигарет в ларьке.")
        elif (how_old_are_u > 150) or (how_old_are_u < 0):
            bot.send_message(chat_id, text="Введен неверный возраст")
        else:
            bot.send_message(chat_id, text="Не могу поверить, что в детстве люди такого возраста казались мне взрослыми.")
    elif ms_text == "Задание 6":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    elif ms_text == "Задание 7":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    elif ms_text == "Задание 8":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    elif ms_text == "Задание 9":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    elif ms_text == "Задание 10":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)



    else:# ...........................................................................................................
        bot.send_message(chat_id, text="Я тебя слышу!!! Ваше сообщение: " + ms_text)

# -----------------------------------------------------------------------
bot.polling(none_stop=True, interval=0) # Запускаем бота

print()
