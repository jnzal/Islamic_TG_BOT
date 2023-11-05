from bot import bot
import threading
from essential.reader import reader
from essential.exceptionf import exceptionf
from chooser.nawawi_chooser import nawawi_chooser
import os
from essential.writer import writer
from essential.constants import *

def nawawi():
    # next message timer
    threading.Timer(nawawi_repeater*h, nawawi).start()
    # ------
    _,_, na_files = next(os.walk("texts/suna_na"))
    # -----
    dic = reader()
#    na = dic["na"]
    un = list(set(dic["sunan_nawawi_list"]))# + dic["all"]))
    sent = []
    for user in un:
        try:
            na = dic["na"][f"{user}"]
            bot.send_message(user, nawawi_chooser(na))
            sent.append(user)
            if na == len(na_files):
                dic["na"][f"{user}"] = 1
            else:
                dic["na"][f"{user}"] = na + 1
        except Exception as arg:
            exceptionf(arg, user=user, dic=dic)
    writer(dic)

