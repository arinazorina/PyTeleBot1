import telebot
from telebot import types


def my_input(bot, chat_id, txt, ResponseHandler):
    message = bot.send_message(chat_id, text=txt)
    bot.register_next_step_handler(message, ResponseHandler)
# -----------------------------------------------------------------------
def my_inputInt(bot, chat_id, txt, ResponseHandler):

    message = bot.send_message(chat_id, text=txt)
    bot.register_next_step_handler(message, my_inputInt_SecondPart, botQuestion=bot, txtQuestion=txt, ResponseHandler=ResponseHandler)
    # bot.register_next_step_handler(message, my_inputInt_return, bot, txt, ResponseHandler)  # то-же самое, но короче

def my_inputInt_SecondPart(message, botQuestion, txtQuestion, ResponseHandler):
    chat_id = message.chat.id
    try:
        if message.content_type != "text":
            raise ValueError
        var_int = int(message.text)
        # данные корректно преобразовались в int, можно вызвать обработчик ответа, и передать туда наше число
        ResponseHandler(botQuestion, chat_id, var_int)
    except ValueError:
        botQuestion.send_message(chat_id,
                         text="Можно вводить ТОЛЬКО целое число в десятичной системе исчисления (символами от 0 до 9)!\nПопробуйте еще раз...")
        my_inputInt(botQuestion, chat_id, txtQuestion, ResponseHandler)  # это не рекурсия, но очень похоже
        # у нас пара процедур, которые вызывают друг-друга, пока пользователь не введёт корректные данные,
        # и тогда этот цикл прервётся, и управление перейдёт "наружу", в ResponseHandler

def dz1(bot, chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    myname = 'Арина'
    bot.send_message(chat_id, text="Привет, меня зовут " + myname)
def dz2(bot, chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    myname = 'Арина'
    myage = '18'
    bot.send_message(chat_id, text="Привет, меня зовут " + myname + ', мне ' + myage)
def dz3(bot, chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    myname = 'Арина'
    myname2 = myname * 5
    bot.send_message(chat_id, text="Мое имя 5 раз подряд: " + myname2)

def dz4(bot, chat_id, message):
    bot.send_message(chat_id, 'Как тебя зовут?')
    bot.register_next_step_handler(message, dz4_1, bot)

def dz4_1( message, bot):
    bot.send_message(message.chat.id, f'Приятно познакомиться, {message.text} \nСколько тебе лет?')
    bot.register_next_step_handler(message, dz4_2, bot)

def dz4_2(message, bot):
    if message.text.isnumeric()== True:
        bot.send_message(message.chat.id, f'Тебе уже {message.text}! Впринципе, выглядишь вполне на свой возраст)')
    while message.text.isnumeric() == False:
        bot.send_message(message.chat.id, 'Введите верный возраст!!')
        break



def dz5(bot, chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)


def dz6(bot, chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    dz6_ResponseHandler = lambda message: bot.send_message(chat_id,
                                                           f"Добро пожаловать {message.text}! У тебя красивое имя, в нём {len(message.text)} букв!")
    my_input(bot, chat_id, "Как тебя зовут?", dz6_ResponseHandler)
def dz7(bot, chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
def dz8(bot, chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
def dz9(bot, chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

def dz10(bot, chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

