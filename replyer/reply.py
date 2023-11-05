from bot import bot
from essential.checker import checker
import os
from essential.reader import reader
from essential.readerr import readerr
from essential.writer import writer
from essential.writerr import writerr
from essential.exceptionf import exceptionf
from chooser.sunah_chooser import sunah_chooser
from chooser.nawawi_chooser import nawawi_chooser
from chooser.estiadah_chooser import estiadah_chooser
from chooser.ayah_chooser import ayah_chooser
from importers.quran import quran, countrf
from importers.duaa import duaa, duaaf
from importers.hesn import hesn, hesnf
from markups.gen_add_cha import gen_add_cha
from markups.gen_help import gen_help
from essential.checker import cha_checker
from bot import BOT_ID
from commands.res_ayah import res_ayah
from commands.res_sunah import res_sunah
from essential.channel_adder import channel_add
from essential.constants import my_id
from essential.deleter import deleter

ayat_list = ["اية" , "قران", "آية", "قرآن", "ayah","ayat", "ايات", "آيات", "estiadah", "إستعاذة", "استعاذة"]
sunah_list = ["suna", "sunah", "سنة", "سنه", "مهجورة", "مهجورة", "حديث"]
greetings = ["hello", "hi", "مرحبا"]

#ui# answeing messages
@bot.message_handler(content_types=["text", "photo", "audio", 'video', 'voice', 'document'])
def reply(message):
    try:
        checker(message.chat.id)
        if message.text:
            words = message.text.split()
            #greeting
            if words[0].lower() in greetings:
                bot.reply_to(message, "أهلًا ومرحبًا، الرجاء استخدام زر البداية لإستخدام البوت", reply_markup=gen_help())
            #ayah
            elif words[0].lower() in ayat_list:
                res_ayah(message)
            #sunah
            elif words[0].lower() in sunah_list:
                res_sunah(message)
            # user deleter
            elif words[0].lower() == "deluser":
                dic = reader()
                if words[1] == "user":
                    if int(words[2]) in dic["users"]:
                        dic["users"].remove(int(words[2]))
                        dic["deluser"].append(int(words[2]))
                        writer(dic)
                        bot.reply_to(message, "user deleted")
                    else:
                        bot.reply_to(message, "user not in users")

            #adding channel
            elif words[0][0] == "@":
                channel_add(words[0], message)

            elif words[0].lower() == "مساعدة":
                bot.reply_to(message, "يرجى التأكد من أنكم قمتم بإرسال التفاصيل في نفس الرسالة، وإظهار الحساب أو كتابة اسم المستخدم الخاص بكم للتواصل معكم")
                bot.forward_message(my_id, message.chat.id, message.id)
            #anything else
            elif message.chat.id != my_id:
                bot.reply_to(message, "إدخال خاطئ، الرجاء الضغط على زر البداية لإستخدام البوت، أو التواصل مع المطور لأي استفسار او مساعدة", reply_markup=gen_help())
                bot.forward_message(chat_id=my_id, from_chat_id=message.chat.id, message_id=message.id)
            elif message.chat.id == my_id:
                dic = reader()
                un = list(set(dic["channels"] + dic["users"]))
                print(un)
                for ch in un:
                    try:
                        bot.copy_message(chat_id=ch, from_chat_id=message.chat.id, message_id=message.id)
                    except Exception as arg:
                        exceptionf(arg, user=ch, dic=dic)
                bot.reply_to(message, "تم إرسال الرسالة إلى كل القنوات المضاف البوت لها")
        else:
            if message.chat.id != my_id:
                bot.reply_to(message, "إدخال خاطئ، الرجاء الضغط على زر البداية لإستخدام البوت، أو التواصل مع المطور لأي استفسار او مساعدة", reply_markup=gen_help())
                bot.forward_message(chat_id=my_id, from_chat_id=message.chat.id, message_id=message.id)
            elif message.chat.id == my_id:
                dic = reader()
                un = list(set(dic["channels"] + dic["users"]))
                for ch in un:
                    try:
                        bot.copy_message(chat_id=ch, from_chat_id=message.chat.id, message_id=message.id)
                    except Exception as arg:
                        exceptionf(arg, user=ch, dic=dic)
                bot.reply_to(message, "تم إرسال الرسالة إلى كل القنوات المضاف البوت لها")

                # if message.caption:
                #     print(message.caption)
    except Exception as arg:
        exceptionf(arg)

