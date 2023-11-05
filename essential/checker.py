from essential.exceptionf import exceptionf
from bot import bot
from essential.constants import my_id
from .reader import reader
from .writer import writer


def checker(mess):
    try:
        dic = reader()
        if mess not in dic["users"]:
            if mess in dic["deluser"]:
                dic["deluser"].remove(mess)
                bot.send_message(my_id, f'tg://user?id={mess} has unblocked us')
            else:
                bot.send_message(my_id, f'you have a new user\n tg://user?id={mess}')
            dic["users"].append(mess)
            if f"{mess}" not in dic["watir_and_duha_reminder_list"]:
                dic["watir_and_duha_reminder_list"].append(mess)
            if f"{mess}" not in dic["white_days_list"]:
                dic["white_days_list"].append(mess)
        if (f"{mess}") not in dic["count"].keys():
            dic["count"][f"{mess}"] = 0
        if (f"{mess}") not in dic["sc"].keys():
            dic["sc"][f"{mess}"] = 1
        if (f"{mess}") not in dic["es"].keys():
            dic["es"][f"{mess}"] = 1
        if (f"{mess}") not in dic["hesnc"].keys():
            dic["hesnc"][f"{mess}"] = 0
        if (f"{mess}") not in dic["na"].keys():
            dic["na"][f"{mess}"] = 1
        writer(dic)
    except Exception as arg:
        exceptionf(arg)
    writer(dic)



def cha_checker(mess):
    try:
        dic = reader()
        if mess not in dic["channels"]: # means its a new channel
            dic["channels"].append(mess)
            dic["watir_and_duha_reminder_list"].append(mess)
            dic["white_days_list"].append(mess)
            print(mess)
            print(dic['channels'])
            bot.send_message(my_id, f"you have a new channel\n{mess}")
        if mess not in dic["count"].keys():
            dic["count"][mess] = 0
        if mess not in dic["sc"].keys():
            dic["sc"][mess] = 1
        if mess not in dic["es"].keys():
            dic["es"][mess] = 1
        if mess not in dic["hesnc"].keys():
            dic["hesnc"][mess] = 0
        if mess not in dic["na"].keys():
            dic["na"][mess] = 1        
    except Exception as arg:
        exceptionf(arg)
    writer(dic)


