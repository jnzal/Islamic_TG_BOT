import time
from essential.writer import writer
from essential.reader import reader
from essential.add_to_list_checker import block_from_all
from essential.add_cha_checker import block_cha_from_all
from essential.constants import my_id
from bot import bot
def deleter(user, dic):
    bot.send_message(my_id, f'bot has been blocked by tg://user?id={user}')
    if user not in dic["blocked_counter"].keys():
        dic["blocked_counter"][user] = 0

    dic["blocked_counter"][user] =  dic["blocked_counter"][user] + 1
    if dic["blocked_counter"][user] > 3 :
        dic['blocked_counter'].pop(user)
        if user in dic['users']:
            dic['users'].remove(user)
            if user not in dic['deluser']:
                dic['deluser'].append(user)
            dic = block_from_all(user, dic)
            bot.send_message(my_id, f'tg://user?id={user} has been deleted')
            
        elif user in dic['channels']:
            dic['channels'].remove(user)
            if user not in dic['delchannel']:
                dic['delchannel'].append(user)
            dic = block_cha_from_all(user, dic)
    return dic
