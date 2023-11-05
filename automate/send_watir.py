from bot import bot
import threading
from essential.writer import writer
from essential.reader import reader
from essential.exceptionf import exceptionf
import os

def send_watir():
    # ----
    _,_, watir_files = next(os.walk("pictures/pic_w"))
    # ----
    dic = reader()
    wc = dic["wc"]
    wc = 1
    sent = []
    text =  "إن الله وتر يحب الوتر"
    ptext = f"texts/text_w/watir_{wc}"
    ppic = f"pictures/pic_w/watir_{wc}"
    if os.path.isfile(ptext):
        text = ""
        with open(ptext, "r") as r:
            for line in r:
                text = text + line
    un = list(set(dic["watir_and_duha_reminder_list"]))# + dic["all"]))
    for user in un:
        try:
            bot.send_photo(user, open(ppic, "rb"), caption=text)
            sent.append(user)
        except Exception as arg:
            exceptionf(arg, user=user, dic=dic)
    if wc == len(watir_files):
        dic["wc"] = 1
    else:
        dic["wc"] = wc + 1
    writer(dic)

