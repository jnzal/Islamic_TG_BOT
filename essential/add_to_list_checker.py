from bot import bot
from .writer import writer
from .reader import reader

lists = ([
  'hesn_list'
, 'quran_list'
, 'sunah_mahjoorah_list'
, 'sunan_nawawi_list'
, 'sunah_estiadah_list'
, 'prayer_list'
, 'watir_and_duha_reminder_list'
, 'qiyam_al_layl_list'
, 'monday_and_thursday_list'
, 'white_days_list'
, 'azkar_mn_list'
, 'duaa_list'
])

def add_to_list_checker(user, lists):
    if user.message.chat.id not in lists:
        lists.append(user.message.chat.id)
        bot.answer_callback_query(user.id, "تمت إضافتك للقائمة بنجاح")
    elif user.message.chat.id in lists:
        lists.remove(user.message.chat.id)
        bot.answer_callback_query(user.id, "تمت إزالتك من القائمة بنجاح")

def add_to_all(user):
    dic = reader()
    for x in lists:
        if user.message.chat.id not in dic[x]:
            dic[x].append(user.message.chat.id)
    bot.answer_callback_query(user.id, "تمت إضافتك لجميع القوائم بنجاح")
    writer(dic)

def remove_from_all(user, **kwargs):
    dic = reader()
    for x in lists:
        if user.message.chat.id in dic[x]:
            dic[x].remove(user.message.chat.id)
    bot.answer_callback_query(user.id, "تمت إزالتك من جميع القوائم بنجاح")
    writer(dic)

def block_from_all(user, dic):
    for x in lists:
        if user in dic[x]:
            dic[x].remove(user)
    return dic



