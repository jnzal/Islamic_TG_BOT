from bot import bot
from essential.exceptionf import exceptionf
from essential.checker import checker

@bot.message_handler(commands=["channel"])
def welcome_channel(message):
    try:
        checker(message.chat.id)
        bot.send_message(message.chat.id, '''
قم بإرسال اسم المستخدم (username) للقناة أو المجموعة الخاصة بك مبدوءا بعلامة @
ويشترط أن يكون البوت مضافا إليها وتم تعيينه كمسؤول
        ''')
    except Exception as arg:
        exceptionf(arg)

