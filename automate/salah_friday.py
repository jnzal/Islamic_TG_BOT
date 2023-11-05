from bot import bot
import threading
from . import *
from essential.reader import reader
from essential.exceptionf import exceptionf

def salah_friday():
    dic = reader()
    sent = []
    un = list(set(dic["users"] + dic["channels"]))
    text = '''من مغربِ يوم الخميس
إلى مغرب الجُمعة تتنزلُ رحمات 
ونفحات فاغتنموها بـ الصلاة على النبي.'''
    pvoice = "voice/salah_ala_nabi"
    for user in un:
        try:
            bot.send_voice(user, open(pvoice,"rb"), timeout=60, duration=193, caption=text)
            sent.append(user)
        except Exception as arg:
            exceptionf(arg, user=user, dic=dic)

