from bot import bot
import threading
from essential.reader import reader
from essential.exceptionf import exceptionf
from essential.constants import *

def azkar_mn():
    # next message timer
#    threading.Timer(azkar_mn_repeater*h, azkar_mn).start()
    # -----
    dic = reader()
    ppic = "pictures/pic_azkar/azkar"
    un = list(set(dic["azkar_mn_list"]))# + dic["all"]))
    sent = []
    for user in un:
        try:
            bot.send_photo(user, open(ppic, "rb"))
            sent.append(user)
        except Exception as arg:
            exceptionf(arg, user=user, dic=dic)
