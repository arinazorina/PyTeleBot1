if ms_text == 'Задание 5':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    how_old_are_u = inputBot(message, "Сколько тебе лет?")
    while how_old_are_u.isnumeric() == False:
        bot.send_message(chat_id, text="Введите верный возраст")
    if int(how_old_are_u > 0) and int(how_old_are_u < 18):
        bot.send_message(chat_id, text="Никто не определит Ваш возраст лучше, чем продавщица сигарет в ларьке.")
    elif int(how_old_are_u > 150) or int(how_old_are_u < 0):
        bot.send_message(chat_id, text="люди столько не живут!")
    else:
        bot.send_message(chat_id, text="Не могу поверить, что в детстве люди такого возраста казались мне взрослыми.")

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


def dz5(bot, chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    def dz5(bot, chat_id):
        my_inputInt(bot, chat_id, "Сколько тебе лет?", dz5_ResponseHandler)

    def dz5_ResponseHandler(bot, chat_id, age_int):
        bot.send_message(chat_id, text=f"О! тебе уже {age_int}! \nА через год будет уже {age_int + 1}!!!")

def dz4(bot, chat_id, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    dz4_ResponseHandler = lambda message: bot.send_message(chat_id,
                                                           f"Привет, {message.text}!")
    name=my_input(bot, chat_id, "Как тебя зовут?", dz4_ResponseHandler)
    bot.register_next_step_handler(message, dz4_1)