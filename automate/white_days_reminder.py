from bot import bot
import threading
from essential.writer import writer
from essential.reader import reader
from essential.exceptionf import exceptionf
import os

def white_days_reminder():
    dic = reader()
    wdr = dic["wdr"]
    # ----
    _,_, wdr_files = next(os.walk("pictures/pic_white_days"))
    # ----
    sent = []
    un = list(set(dic["white_days_list"]))# + ['all']))
    text = '"أوصاني خليلي ألّا أترك ثلاثًا، صلاة الضحى والوتر، وصيام ثلاثٍ من كل شهر"'
    ppic = f"pictures/pic_white_days/wd_{wdr}"
    ptext = f"texts/text_white_days/wd_{wdr}"
    if os.path.isfile(ptext):
        text = ""
        with open(ptext, "r") as r:
            for line in r:
                text = text + line
    for user in un:
        try:
            bot.send_photo(user, open(ppic, "rb"), caption = text)
            sent.append(user)
        except Exception as arg:
            exceptionf(arg, user=user, dic=dic)
    if wdr == len(wdr_files):
        dic["wdr"] = 1
    else:
        dic["wdr"] = wdr + 1
    writer(dic)

