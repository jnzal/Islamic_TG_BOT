from bot import bot
import threading
from essential.writer import writer
from essential.reader import reader
from chooser.duaa_chooser import duaa_chooser
from essential.exceptionf import exceptionf
from importers.duaa import duaa, duaaf
from essential.constants import *

def send_duaa():
    # next message timer
    t_duaa = threading.Timer(duaa_repeater*h, send_duaa)
    t_duaa.name = "duaa timer"
    t_duaa.start()
    # -----
    
    dic = reader()
    sent = []
    un = list(set(dic["duaa_list"]))# + dic["all"]))
    for user in un:
        if f"{user}" not in dic["duaac"].keys():
            dic["duaac"][f"{user}"] = 0
            writer(dic)
        try:
            dic = reader()
            c = dic["duaac"][f"{user}"]
            bot.send_message(user, duaa_chooser(c))
            sent.append(user)
            if c == duaaf:
                dic["duaac"][f"{user}"] = 0
            else:
                dic["duaac"][f"{user}"] = c + 1
        except Exception as arg:
            exceptionf(arg, user=user, dic=dic)
    writer(dic)
