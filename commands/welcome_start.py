from bot import bot
from essential.checker import checker
from essential.exceptionf import exceptionf
from markups.gen_start import gen_start

@bot.message_handler(commands=["start"])
def welcome_start(message):
    try:
        checker(message.chat.id)
        bot.send_message(message.chat.id, '''
السلام عليكم ورحمة الله وبركاته، تحيّة الإسلام وتحيّة أهل الجنة
لا إله إلا الله، بها نحيا وعليها نموت وبها نلقى وجه الله،
أهلا بك في بوت آيات الذكر الحكيم

نحتسبه عند الله صدقة جارية عن أموات المسلمين كافة

دام الله في عوننا على ذكره وشكره وحسن عبادته
        ''', reply_markup=gen_start())
    except Exception as arg:
        exceptionf(arg)

