from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def gen_add_cha():

    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(                 InlineKeyboardButton("الإضافة لكل القوائم", callback_data="add_cha_all"),
                                InlineKeyboardButton("الإزالة من كل القوائم", callback_data="rem_cha_all"),
                                InlineKeyboardButton("قائمة القرآن", callback_data="cha_qur"),
                                InlineKeyboardButton("حصن المسلم", callback_data="cha_hes"),
                                InlineKeyboardButton("السنن المهجورة", callback_data="cha_mah"),
                                InlineKeyboardButton("الأربعين النووية", callback_data="cha_naw"),
                                InlineKeyboardButton("أحاديث الإستعاذة", callback_data="cha_est"),
                                InlineKeyboardButton("تنبيهات الصلاة", callback_data="cha_pra"),
                                InlineKeyboardButton("الوتر والضحى", callback_data="cha_wat"),
                                InlineKeyboardButton("قيام الليل", callback_data="cha_qiy"),
                                InlineKeyboardButton("صيام اثنين وخميس", callback_data="cha_tmf"),
                                InlineKeyboardButton("الأيام البيض", callback_data="cha_thr"),
                                InlineKeyboardButton("أذكار الصباح والمساء", callback_data="cha_azk"),
                                InlineKeyboardButton("الأدعية", callback_data="cha_dua"),
                                InlineKeyboardButton("لإستطلاع القوائم الفعالة لقناتك", callback_data="collect_cha"))
    markup.add(                 InlineKeyboardButton("السابق  <<", callback_data="back"))

    return markup


