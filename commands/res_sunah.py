from bot import bot
from essential.checker import checker
from essential.reader import reader
from essential.exceptionf import exceptionf
from essential.writer import writer
import random
import os
from chooser.sunah_chooser import sunah_chooser
from chooser.nawawi_chooser import nawawi_chooser
from chooser.estiadah_chooser import estiadah_chooser
from essential.checker import checker
sunah_list = ["suna", "sunah", "سنة", "سنه", "مهجورة", "مهجورة", "حديث"]

@bot.message_handler(commands=sunah_list)
def res_sunah(message):
    try:
        checker(message.chat.id)
        dic = reader()
        suna_functions = [sunah_chooser, nawawi_chooser, estiadah_chooser]
        import random
        ran = random.choice(suna_functions)
        if (str(ran)).split()[1] == (str(suna_functions[0])).split()[1]:
            c = dic["sc"][f"{message.chat.id}"]
            t = "sc"
            q = f"{message.chat.id}"
            _, _, b = next(os.walk("texts/suna"))
            a = len(b)
        elif (str(ran)).split()[1] == (str(suna_functions[1])).split()[1]:
            c = dic["na"][f"{message.chat.id}"]
            t = "na"
            q = f"{message.chat.id}"
            _, _, b = next(os.walk("texts/suna_na"))
            a = len(b)
        elif (str(ran)).split()[1] == (str(suna_functions[2])).split()[1]:
            c = dic["es"][f"{message.chat.id}"]
            t = "es"
            q = f"{message.chat.id}"
            _, _, b = next(os.walk("texts/suna_es"))
            a = len(b)
        bot.send_message(message.chat.id, ran(c))
        if c == a:
            dic[t][q] = 1
        else:
            dic[t][q] = c + 1
        writer(dic)
    except Exception as arg:
        print(arg)



