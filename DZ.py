import telebot
from telebot import types

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

