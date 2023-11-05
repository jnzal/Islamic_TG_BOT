from essential.reader import reader
from bot import bot

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
dc ={'hesn_list' : "حصن المسلم"
, 'quran_list' : "قائمة القرآن الكريم"
, 'sunah_mahjoorah_list' : "السنن المهجورة"
, 'sunan_nawawi_list' : "الأربعين النووية"
, 'sunah_estiadah_list' : "أحاديث الإستعاذة"
, 'prayer_list' : "تنبيهات الصلاة"
, 'watir_and_duha_reminder_list' : "الوتر والضحى"
, 'qiyam_al_layl_list' : "قيام الليل"
, 'monday_and_thursday_list' : "صيام إثنين وخميس"
, 'white_days_list' : "الأيام البيض"
, 'azkar_mn_list' : "أذكار الصباح والمساء"
, 'duaa_list' : "الأدعية"

}

def collector(user):
    dic = reader()
    text = ''
    num = 0
    for x in lists:
        if user.message.chat.id in dic[x]:
            text += f'{dc[x]}\n'
            num += 1
    text += f"عدد القوائم الفعالة لديك هو {num}"
   # if text == '':
    #    text = 'ليس لديك أي قائمة فعالة'
    bot.send_message(user.message.chat.id, text)
    bot.answer_callback_query(user.id, "هذه القوائم الفعالة لديك")


def cha_collector(user):
    dic = reader()
    text = ''
    num = 0
    word = dic["admins"][user.message.chat.id]
    for x in lists:
        if word in dic[x]:
            text += f'{dc[x]}\n'
            num += 1
    #= len(text.split())
    text += f"\n عدد القوائم الفعّالة للقناة  هو {num}"
   # if text == '':
      #  text = 'ليس لديك أي قائمة فعالة'
    bot.send_message(user.message.chat.id, text)
    bot.answer_callback_query(user.id, "هذه القوائم الفعالة لديك")
