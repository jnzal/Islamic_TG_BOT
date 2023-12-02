from bot import bot
import threading
from essential.writer import writer
from essential.reader import reader
from essential.exceptionf import exceptionf
from chooser.hesn_chooser import hesn_chooser
from importers.hesn import hesn, hesnf
from essential.constants import *

def send_hesn():
    # next message timer
    t_hesn = threading.Timer(hesn_repeater*h, send_hesn)
    t_hesn.name = "hesn timer"
    t_hesn.start()
    # ------

    dic = reader()
    sent = []
    un = list(set(dic["hesn_list"]))# + dic["all"]))
    for user in un:
        if f"{user}" not in dic["hesnc"].keys():
            dic["hesnc"][f"{user}"] = 1
            writer(dic)
        try:
            dic = reader()
            c = dic["hesnc"][f"{user}"]
            bot.send_message(user, hesn_chooser(c))
            sent.append(user)
            if c == hesnf:
                dic["hesnc"][f"{user}"] = 0
            else:
                dic["hesnc"][f"{user}"] = c + 1
        except Exception as arg:
            exceptionf(arg, user=user, dic=dic)
    writer(dic)
