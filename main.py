#!/usr/bin/python3.10
#importing
##from essential.reporter import reporter
from prayertime.nextprayer import nextprayer
from bot import main, bot
from timer.timer import timer
from essential.reader import reader
from essential.writer import writer
from essential.readerr import readerr
from commands.welcome_add import welcome_add
from commands.welcome_channel import welcome_channel
from commands.welcome_help import welcome_help
from commands.welcome_start import welcome_start
from commands.res_ayah import res_ayah
from commands.res_sunah import res_sunah
from replyer.reply import reply
from callback.callback import callback_query
from essential.exceptionf import exceptionf

#---
timer()
nextprayer()
dic = reader()
if "blocked_counter" not in dic.keys():
    dic["blocked_counter"] = {}
if 'delchannel' not in dic.keys():
    dic['delchannel'] = []
writer(dic)
# print(dic)
channmin = readerr()

print("users " + str(dic["users"]))
print("channels " + str(dic["channels"]))


#=-=-=-=-=-=-=-=-=-#=-=-=-=-=-=-=-=-=-#=-=-=-=-=-=-=-=-=-#=-=-=-=-=-=-=-=-=-
main()
##
##
