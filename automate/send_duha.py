from bot import bot
import threading
from essential.writer import writer
from essential.reader import reader
from essential.exceptionf import exceptionf
import os

def send_duha():
    # ----
    _,_, duha_files = next(os.walk("pictures/pic_d"))
    # ----
    dic = reader()
    dc = dic["dc"]
    sent = []
    text = "صلاة الضحى أثابكم الله، تعدل 360 صدقة وهي بعدد مفاصل جسدك، وتقرّبك من الله -جل في علاه-، يصبح على كل سلامى من أحدكم صدقة."
    ptext = f"texts/text_d/duha_{dc}"
    ppic = f"pictures/pic_d/duha_{dc}"
    if os.path.isfile(ptext):
        text = ""
        with open(ptext, "r") as r:
            for line in r:
                text = text + line
    un = list(set(dic["watir_and_duha_reminder_list"]))# + dic["all"]))
    for user in un:
        try:
            bot.send_photo(user, open (ppic,'rb'), caption=text)
            sent.append(user)
        except Exception as arg:
            exceptionf(arg, user=user, dic=dic)
    if dc == len(duha_files):
        dic["dc"] = 1
    else:
        dic["dc"] = dc + 1
    writer(dic)

