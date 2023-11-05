from .reader import reader
from bot import bot
from .writer import writer

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
, 'duaa_list'])

def add_cha_checker(user, lists):
    try:
        dic = reader()
        word = dic["admins"][user.message.chat.id]
        if word not in lists:
            lists.append(word)
            bot.answer_callback_query(user.id, f"تمت إضافة قناة {word} للقائمة بنجاح")
        elif word in lists:
            lists.remove(word)
            bot.answer_callback_query(user.id, f"تمت إزالة القناة {word} من القائمة بنجاح", cache_time=10)
    except NameError:
        bot.send_message(call.message.chat.id, '''
    قم بإرسال اسم المستخدم (username) للقناة أو المجموعة الخاصة بك مبدوءا بعلامة @
    ''')

def add_cha_to_all(user):
    dic = reader()
    word = dic["admins"][user.message.chat.id]
    for x in lists:
        if word not in dic[x]:
            dic[x].append(word)
    bot.answer_callback_query(user.id, f"تمت إضافة قناة {word} إلى جميع القوائم بنجاح")
    writer(dic)

def remove_cha_from_all(user, dic):
    word = dic["admins"][user.message.chat.id]
    for x in lists:
        if word in dic[x]:
            dic[x].remove(word)
    bot.answer_callback_query(user.id, f"تمت إزالة قناة {word} من جميع القوائم بنجاح")
    return dic


# def remove_cha_from_all(user):
#     dic = reader()
#     word = dic["admins"][user.message.chat.id]
#     for x in lists:
#         if word in dic[x]:
#             dic[x].remove(word)
#     bot.answer_callback_query(user.id, f"تمت إزالة قناة {word} من جميع القوائم بنجاح")
#     writer(dic)

def block_cha_from_all(user, dic):
    for x in lists:
        if user in dic[x]:
            dic[x].remove(user)
    return dic
