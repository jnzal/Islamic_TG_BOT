from bot import bot
import threading
from essential.writer import writer
from essential.reader import reader
from essential.exceptionf import exceptionf
import os

def send_adha10():
# --
    _,_, adha10_files = next(os.walk("pictures/pic_adha10"))
# --
    dic = reader()
    sent = []
    un = list(set(dic["users"] + dic["channels"]))# + dic["all"]))
    c = dic["adha10c"]
    text = ' عَنِ ابْنِ عَبَّاسٍ رَضِيَ اللهُ عَنْهُمَا قَالَ: قَالَ رَسُولُ اللهِ -صلى الله عليه وسلم-: «مَا مِنْ أَيَّامٍ العَمَلُ الصَّالِحُ فِيهِنَّ أَحَبُّ إِلَى اللهِ مِنْ هَذِهِ الأَيَّامِ العَشْرِ، فَقَالُوا: يَا رَسُولَ اللهِ، وَلا الجِهَادُ فِي سَبِيلِ اللهِ؟.. فَقَالَ رَسُولُ اللهِ -صلى الله عليه وسلم-: «وَلا الجِهَادُ فِي سَبِيلِ اللهِ، إِلَّا رَجُلٌ خَرَجَ بِنَفْسِهِ وَمَالِهِ فَلَمْ يَرْجِعْ مِنْ ذَلِكَ بِشَيْءٍ» أخرجه الترمذي.'
    ppic = f"pictures/pic_adha10/adha10_{c}"
    ptext = f"texts/text_adha10/adha10_{c}"
    if os.path.isfile(ptext):
        text = ""
        with open(ptext, "r") as r:
            for line in r:
                text = text + line
    if os.path.isfile(ppic) is False:
            ppic = f"pictures/pic_adha10/adha10_{1}"
    for user in un:
        try:
            bot.send_photo(user, open(ppic, "rb"), caption = text)
            sent.append(user)
        except Exception as arg:
            exceptionf(arg, user=user, dic=dic)
    if c == len(adha10_files):
        dic["adha10c"] = 0
    else:
        dic["adha10c"] = c + 1
    writer(dic)
