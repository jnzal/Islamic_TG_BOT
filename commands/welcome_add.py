from bot import bot
from essential.exceptionf import exceptionf
from markups.gen_add import gen_add
from essential.checker import checker

@bot.message_handler(commands=["add"])
def welcome_add(message):
    try:
        checker(message.chat.id)
        bot.send_message(message.chat.id, '''
قم بالضغط على القائمة لإضافتك إليها:
تم بالفعل إضافتك لقائمة التذكير بصلاتيّ الوتر والضحى، وصيام الأيام البيض من كل شهر، لأن حبيبنا ﷺ ما تركها لا في سفر ولا في حضر
دام الله في عوننا على ذكره وشكره وحسن عبادته
        ''', reply_markup=gen_add())
    except Exception as arg:
        exceptionf(arg)

