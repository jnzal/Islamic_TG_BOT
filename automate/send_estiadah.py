from bot import bot
import threading
from essential.writer import writer
from essential.reader import reader
from essential.exceptionf import exceptionf
from chooser.estiadah_chooser import estiadah_chooser
from essential.constants import *
import os

def send_estiadah():
    # next message timer
    t_estiadah = threading.Timer(estiadah_repeater*h, send_estiadah)
    t_estiadah.name = "estiadah timer"
    t_estiadah.start()
    # ------
    _,_, es_files = next(os.walk("texts/suna_es"))
    # ----
    dic = reader()
#    es = dic["es"]
    un = list(set(dic["estiadah_list"]))
    sent = []
    for user in un:
        try:
            dic = reader()
            es = dic['es'][f'{user}']
            bot.send_message(user, estiadah_chooser(es))
            sent.append(user)
        except Exception as arg:
            exceptionf(arg, user=user, dic=dic)
        
        if es == len(es_files):
            dic["es"][f"{user}"] = 1
        else:
            dic["es"][f"{user}"] = es + 1
    writer(dic)

