from essential.checker import checker
from chooser.sunah_chooser import sunah_chooser
from chooser.nawawi_chooser import nawawi_chooser
from chooser.estiadah_chooser import estiadah_chooser
from bot import bot
import os
from essential.exceptionf import exceptionf
from essential.reader import reader
from essential.writer import writer
from essential.add_to_list_checker import add_to_list_checker, add_to_all, remove_from_all
from essential.add_cha_checker import add_cha_checker, add_cha_to_all, remove_cha_from_all
from essential.collector import collector, cha_collector
from markups.gen_add import gen_add
from markups.gen_channel import gen_channel
from markups.gen_start import gen_start
from markups.gen_add_cha import gen_add_cha
from markups.gen_help import gen_help
from commands.res_ayah import res_ayah
from commands.res_sunah import res_sunah
j_sally = "صلّ على الحبيب ﷺ"

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    dic = reader()
    if call.data == "add_all":
        add_to_all(call)
    elif call.data == "rem_all":
        remove_from_all(call)
    elif call.data == "add_cha_all":
        add_cha_to_all(call)
    elif call.data == "rem_cha_all":
        remove_cha_from_all(call)
    elif call.data == "collect":
        collector(call)
    elif call.data == "collect_cha":
        cha_collector(call)
    elif call.data == "add_hes":
        add_to_list_checker(call, dic['hesn_list'])
        writer(dic)
    elif call.data == "add_qur":
        add_to_list_checker(call, dic['quran_list'])
        writer(dic)
    elif call.data == "add_mah":
        add_to_list_checker(call, dic['sunah_mahjoorah_list'])
        writer(dic)
    elif call.data == "add_naw":
        add_to_list_checker(call, dic['sunan_nawawi_list'])
        writer(dic)
    elif call.data == "add_est":
        add_to_list_checker(call, dic['sunah_estiadah_list'])
        writer(dic)
    elif call.data == "add_pra":
        add_to_list_checker(call, dic['prayer_list'])
        writer(dic)
    elif call.data == "add_wat":
        add_to_list_checker(call, dic['watir_and_duha_reminder_list'])
        writer(dic)
    elif call.data == "add_qiy":
        add_to_list_checker(call, dic['qiyam_al_layl_list'])
        writer(dic)
    elif call.data == "add_tmf":
        add_to_list_checker(call, dic['monday_and_thursday_list'])
        writer(dic)
    elif call.data == "add_thr":
        add_to_list_checker(call, dic['white_days_list'])
        writer(dic)
    elif call.data == "add_azk":
        add_to_list_checker(call, dic['azkar_mn_list'])
        writer(dic)
    elif call.data == "add_dua":
        add_to_list_checker(call, dic['duaa_list'])
        writer(dic)
    elif call.data == "cha_hes":
        add_cha_checker(call, dic['hesn_list'])
        writer(dic)
    elif call.data == "cha_qur":
        add_cha_checker(call, dic['quran_list'])
        writer(dic)
    elif call.data == "cha_mah":
        add_cha_checker(call, dic['sunah_mahjoorah_list'])
        writer(dic)
    elif call.data == "cha_naw":
        add_cha_checker(call, dic['sunan_nawawi_list'])
        writer(dic)
    elif call.data == "cha_est":
        add_cha_checker(call, dic['sunah_estiadah_list'])
        writer(dic)
    elif call.data == "cha_pra":
        add_cha_checker(call, dic['prayer_list'])
        writer(dic)
    elif call.data == "cha_wat":
        add_cha_checker(call, dic['watir_and_duha_reminder_list'])
        writer(dic)
    elif call.data == "cha_qiy":
        add_cha_checker(call, dic['qiyam_al_layl_list'])
        writer(dic)
    elif call.data == "cha_tmf":
        add_cha_checker(call, dic['monday_and_thursday_list'])
        writer(dic)
    elif call.data == "cha_thr":
        add_cha_checker(call, dic['white_days_list'])
        writer(dic)
    elif call.data == "cha_azk":
        add_cha_checker(call, dic['azkar_mn_list'])
        writer(dic)
    elif call.data == "cha_dua":
        add_cha_checker(call, dic['duaa_list'])
        writer(dic)
    elif call.data == "add":
        bot.edit_message_text(text = '''
قم بالضغط على القائمة لإضافتك إليها:
تم بالفعل إضافتك لقائمة التذكير بصلاتيّ الوتر والضحى، وصيام الأيام البيض من كل شهر، لأن حبيبنا ﷺ ما تركها لا في سفر ولا في حضر
دام الله في عوننا على ذكره وشكره وحسن عبادته
        ''', chat_id = call.message.chat.id, message_id=call.message.message_id, reply_markup = gen_add())
        bot.answer_callback_query(call.id, j_sally)
    elif call.data == "channel":
        bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = '''
قم بإرسال اسم المستخدم (username) الخاص بالقناة أو المجموعة الخاصة بك مبدوءا بعلامة @
ويشترط أن يكون البوت مضافا إليها وتم تعيينه كمسؤول في القنوات
        ''', reply_markup=gen_channel())
        bot.answer_callback_query(call.id, j_sally)
    elif call.data == "back":
        bot.edit_message_text(text = '''
        لإستطلاع القوائم يرجى الضغط على زر القوائم
لإضافة قناتك أو مجموعتك إلى القوائم قم بالضغط على زر القنوات والمجموعات 

دام الله في عوننا على ذكره وشكره وحسن عبادته
''',
                              chat_id = call.message.chat.id,
                              message_id=call.message.message_id,
                              reply_markup=gen_start())
        bot.answer_callback_query(call.id, j_sally)
    elif call.data == "start":
        bot.edit_message_text(text = '''
السلام عليكم ورحمة الله وبركاته، تحيّة الإسلام وتحيّة أهل الجنة
لا إله إلا الله، بها نحيا وعليها نموت وبها نلقى وجه الله،
أهلا بك في بوت آي الذكر الحكيم

نحتسبه عند الله صدقة جارية عن أموات المسلمين كافة

دام الله في عوننا على ذكره وشكره وحسن عبادته        
        ''',
                              chat_id = call.message.chat.id,
                              message_id=call.message.message_id,
                              reply_markup=gen_start())
        bot.answer_callback_query(call.id, j_sally)
    elif call.data == "help":
        bot.edit_message_text(text = '''
يستخدم هذا البوت لإستلام الآيات، الأحاديث النبوية الشريفة، وتذكيرات دينية بشكل أوتوماتيكي،
يمكنك إستلام آية أو حديث فورا بإرسال "آية" أو "حديث" إلى البوت

لإستخدام التذكيرات الأوتوماتيكية، يرجى النقر على زر البداية، للإستفسار الرجاء التواصل مع المطور
        ''',
                              chat_id = call.message.chat.id,
                              message_id=call.message.message_id,
                              reply_markup=gen_help())
        bot.answer_callback_query(call.id, j_sally)
    elif call.data == "ayah":
        bot.answer_callback_query(call.id, j_sally)
        res_ayah(call.message)
    elif call.data == "sunah":
        res_sunah(call.message)
        bot.answer_callback_query(call.id, j_sally)

