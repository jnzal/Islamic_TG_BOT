from bot import bot
import threading
from . import *
from essential.reader import reader
from essential.exceptionf import exceptionf
from essential.add_to_list_checker import block_from_all
from essential.add_cha_checker import remove_cha_from_all
from essential.constants import *


def kahf_friday():
    dic = reader()
    sent = []
    un = list(set(dic["users"] + dic["channels"]))
    text = "عن أبي سَعيدٍ الخُدريِّ عنِ النبيِّ صلَّى اللهُ عليه وسلَّم أنَّه قال: ((مَن قَرَأَ سورةَ الكَهفِ يومَ الجُمُعةِ أضاءَ له من النورِ ما بَينَ الجُمُعتينِ ))"
    pvoice = "voice/kahf"
    for user in un:
        try:
            bot.send_voice(user, open(pvoice,"rb"), timeout=60, duration=1345, caption=text)
            sent.append(user)
        except Exception as arg:
            exceptionf(arg, user=user, dic=dic)

