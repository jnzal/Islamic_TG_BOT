import sys
import os
from bot import bot, BOT_ID
from essential.checker import cha_checker
from markups.gen_add_cha import gen_add_cha
from essential.writer import writer
from essential.writerr import writerr
from essential.reader import reader
from essential.readerr import readerr
from essential.exceptionf import exceptionf

def channel_add(channel, message):
    try:
        dic = reader()
        admins = readerr()
        if (bot.get_chat_member(chat_id=channel, 
            user_id=BOT_ID).status in ["administrator", "member"]):
            cha_checker(channel)
            dic = reader()
            bot.reply_to(message, '''
    قم بالضغط على القائمة المطلوب إضافة/إزالة قناتك/مجموعتك إليها
    ''', reply_markup=gen_add_cha())
            if f"{message.chat.id}" not in admins.keys():
                admins[f"{message.chat.id}"] = []
            if channel not in admins[f"{message.chat.id}"]:
                admins[f"{message.chat.id}"].append(channel)
            writerr(admins)
            dic["admins"][message.chat.id] = channel
            writer(dic)

        else:
            bot.reply_to(message, '''
        الرجاء التأكد من أن البوت مضاف للقناة
        ''')
    except Exception as arg:
        if "chat not found" in str(arg):
            bot.reply_to(message, '''
            اسم المستخدم غير صحيح، الرجاء التأكد من كتابته
            ''')
        else:
            exceptionf(arg)
            # import os
            # import sys
            # exc_type, exc_obj, exc_tb = sys.exc_info()
            # fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            # logging.error(f"{exc_type, fname, exc_tb.tb_lineno}")
