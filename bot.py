from decouple import config
import telebot
from telebot import apihelper
import threading
from essential.constants import h, m
# from essential.exceptionf import exceptionf

BOT_TOKEN = config('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)
apihelper.proxy = {'http':'http://proxy.server:3128'}
BOT_ID = config('BOT_ID')

def main():
    try:
        bot.infinity_polling(timeout = 100)# long_polling_timeout = 50)
    # except Exception as arg:
    #     exceptionf(arg)
    finally:
        t_bot = threading.Timer(2*m, main)
        t_bot.name = "bot_re-executor"
        t_bot.start()
        pass

