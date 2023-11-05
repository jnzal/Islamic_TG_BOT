from bot import bot
import threading
from essential.reader import reader
from essential.exceptionf import exceptionf

def prayerazkar():
    dic = reader()
    sent = []
    ppic = "pictures/pic_azkar/prayer"
    un = list(set(dic["prayer_list"]))# + dic["all"]))
    for user in un:
        try:
            bot.send_photo(user, open(ppic, "rb"))
            sent.append(user)
        except Exception as arg:
            exceptionf(arg, user=user, dic=dic)
