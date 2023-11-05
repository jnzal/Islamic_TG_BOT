from bot import bot
import threading
from essential.reader import reader
from essential.writer import writer
from essential.exceptionf import exceptionf
import os
from essential.constants import m, h
from automate.prayerazkar import prayerazkar

def prayerreminder():
    dic = reader()
    pc = dic["pc"]
    # ----
    _,_, salah_files = next(os.walk("pictures/pic_salah"))
    # ----
    sent = []
    un = list(set(dic["prayer_list"]))# + dic["all"]))
    text = '"آخر وصايا الرسول -عليه الصلاة والسلام- كانت الصلاة "الصلاة، وما ملكت أيمانكم"، صلّوا صلاة مودّع، فلا تدري نفس ماذا تكسب غدًا، ولا تدري نفس بأي أرض تموت"'
    ppic = f"pictures/pic_salah/salah_{pc}"
    ptext = f"texts/text_salah/salah_{pc}"
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
    if pc == len(salah_files):
        dic["pc"] = 1
    else:
        dic["pc"] = pc + 1
    writer(dic)
    t_prayeraz = threading.Timer(15*m, prayerazkar)
    t_prayeraz.name = "prayer_azkar_timer"
    t_prayeraz.start()

