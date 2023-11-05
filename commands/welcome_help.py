from bot import bot
from essential.checker import checker
from essential.exceptionf import exceptionf
from markups.gen_help import gen_help

@bot.message_handler(commands=["help"])
def welcome_help(message):
    try:
        checker(message.chat.id)
        bot.send_message(message.chat.id, '''
يستخدم هذا البوت لإستلام الآيات، الأحاديث النبوية الشريفة، وتذكيرات دينية بشكل أوتوماتيكي،
يمكنك إستلام آية أو حديث فورا بالضغط على الزر المخصص

لإستخدام التذكيرات الأوتوماتيكية، يرجى النقر على زر البداية، للإستفسار الرجاء التواصل مع المطور
        ''', reply_markup=gen_help())
    except Exception as arg:
        exceptionf(arg)

