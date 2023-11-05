from bot import bot
import threading
from essential.reader import reader
from essential.exceptionf import exceptionf
import os
from essential.writer import writer

def qiyam():
    dic = reader()
    c = dic["qiyamc"]
    # ----
    _,_, qiyam_files = next(os.walk("pictures/pic_qiyam"))
    # ----
    sent = []
    un = list(set(dic["qiyam_al_layl_list"]))# + dic["all"]))
    text = ' روى الحاكم في المستدرك عن سهل بن سعد ـ رضي الله عنه ـ قال: جاء جبريل عليه السلام إلى النبي صلى الله عليه وسلم، فقال: يا محمد عش ما شئت، فإنك ميت، وأحبب من أحببت فإنك مفارقه، واعمل ما شئت، فإنك مجزي به، ثم قال يا محمد: شرف المؤمن قيام الليل، وعزه استغناؤه عن الناس.'
    ppic = f"pictures/pic_qiyam/qiyam_{c}"
    ptext = f"texts/text_qiyam/qiyam_{c}"
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
    if c == len(qiyam_files):
        dic["qiyamc"] = 1
    else:
        dic["qiyamc"] = c + 1
    writer(dic)

