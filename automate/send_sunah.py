from bot import bot
import threading
from essential.writer import writer
from essential.reader import reader
from essential.exceptionf import exceptionf
from chooser.sunah_chooser import sunah_chooser
import os
from essential.constants import *

def send_sunah():
    dic = reader()
#    sc = dic["sc"]
    # next message timer
    t_sunah = threading.Timer(sunah_repeater*h, send_sunah)
    t_sunah.name = "sunah timer"
    t_sunah.start()
    # -----
    _,_, suna_files = next(os.walk("texts/suna"))
    # -----
    un = list(set(dic["sunah_mahjoorah_list"]))# + dic["all"]))
    sent = []
    for user in un:
        try:
            dic = reader()
            sc = dic['sc'][f'{user}']
            ppic = f"pictures/pic_suna/suna_{sc}"
            if os.path.isfile(ppic):
                bot.send_photo(user, open(ppic, "rb"), caption=sunah_chooser(sc))
                sent.append(user)
            else:
                bot.send_message(user, sunah_chooser(sc))
                sent.append(user)
            if sc == len(suna_files):
               dic["sc"][f"{user}"] = 1
            else:
                dic["sc"][f"{user}"] = sc + 1

        except Exception as arg:
            exceptionf(arg, user=user, dic=dic)

    writer(dic)

