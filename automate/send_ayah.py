from bot import bot
import threading
from essential.writer import writer
from essential.reader import reader
from essential.exceptionf import exceptionf
from chooser.ayah_chooser import ayah_chooser
from importers.quran import quran, countrf
from essential.constants import *


def send_ayah():
    # next message timer
    threading.Timer(ayah_repeater*h, send_ayah).start()
    # -----
    dic = reader()
    sent = []
    un = list(set(dic["quran_list"]))# + dic['all']))
    for user in un:
        try:
            dic = reader()
            c = dic["count"][f"{user}"]
            bot.send_message(user, ayah_chooser(c))
            sent.append(user)
            if c == countrf:
                dic["count"][f"{user}"] = 0
            else:
                dic["count"][f"{user}"] = c + 1
            writer(dic)
        except Exception as arg:
            exceptionf(arg, user=user, dic=dic)



