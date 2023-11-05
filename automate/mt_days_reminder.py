from bot import bot
import threading
from essential.writer import writer
from essential.reader import reader
from essential.exceptionf import exceptionf
import os

def mt_days_reminder():
    dic = reader()
    mtr = dic["mtr"]
    # ----
    _,_, mtr_files = next(os.walk("pictures/pic_mt"))
    # ----
    sent = []
    un = list(set(dic["monday_and_thursday_list"]))# + dic["all"]))
    text = 'قالت عائشة رضي الله عنها: (كان النبي يصوم حتى نقول: لا يفطر، ويفطر حتى نقول: لا يصوم)'
    ppic = f"pictures/pic_mt/mt_{mtr}"
    ptext = f"texts/text_mt/mt_{mtr}"
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
    if mtr == len(mtr_files):
        dic["mtr"] = 1
    else:
        dic["mtr"] = mtr + 1
    writer(dic)

