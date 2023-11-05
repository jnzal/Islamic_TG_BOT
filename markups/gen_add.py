from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
def gen_add():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(                 InlineKeyboardButton("الإضافة لكل القوائم", callback_data="add_all"),
                                InlineKeyboardButton("الإزالة من كل القوائم", callback_data="rem_all"),
                                InlineKeyboardButton("قائمة القرآن", callback_data="add_qur"),
                                InlineKeyboardButton("حصن المسلم", callback_data="add_hes"),
                                InlineKeyboardButton("السنن المهجورة", callback_data="add_mah"),
                                InlineKeyboardButton("الأربعين النووية", callback_data="add_naw"),
                                InlineKeyboardButton("أحاديث الإستعاذة", callback_data="add_est"),
                                InlineKeyboardButton("تنبيهات الصلاة", callback_data="add_pra"),
                                InlineKeyboardButton("الوتر والضحى", callback_data="add_wat"),
                                InlineKeyboardButton("قيام الليل", callback_data="add_qiy"),
                                InlineKeyboardButton("صيام اثنين وخميس", callback_data="add_tmf"),
                                InlineKeyboardButton("الأيام البيض", callback_data="add_thr"),
                                InlineKeyboardButton("أذكار الصباح والمساء", callback_data="add_azk"),
                                InlineKeyboardButton("الأدعية", callback_data="add_dua"),
                                InlineKeyboardButton("لمعرفة القوائم الفعالة لديك", callback_data="collect"))
    markup.add(                 InlineKeyboardButton("السابق  <<", callback_data="back"))
    return markup


