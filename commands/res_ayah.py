from bot import bot
import threading
from essential.reader import reader
from essential.exceptionf import exceptionf
from essential.writer import writer
from chooser.ayah_chooser import ayah_chooser
from essential.checker import checker
from importers.quran import quran, countrf
from essential.constants import my_id


ayat_list = ["اية" , "قران", "آية", "قرآن", "ayah","ayat", "ايات", "آيات", "estiadah", "إستعاذة", "استعاذة"]

@bot.message_handler(commands=ayat_list)
def res_ayah(message):
    try:
        dic = reader()
        checker(message.chat.id)
        c = dic["count"][f"{message.chat.id}"]
        bot.send_message(message.chat.id, ayah_chooser(c))
        if c == countrf:
            dic["count"][f"{message.chat.id}"] = 1
        else:
            dic["count"][f"{message.chat.id}"] = c + 1
        writer(dic)
    except Exception as arg:
        if 'too long' in str(arg):
            bot.send_message(my_id, 'bot has a problem, the text was too long, check what happened')
        exceptionf(arg, user=user, dic=dic)

