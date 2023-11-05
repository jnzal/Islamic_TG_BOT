from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def gen_start():
    keyboard = InlineKeyboardMarkup()
    keyboard.row_width = 2
    keyboard.add(       InlineKeyboardButton('إستطلاع القوائم الأوتوماتيكية', callback_data='add'))
    keyboard.add(       InlineKeyboardButton('لإستخدام البوت في قناة أو مجموعة', callback_data='channel'))
    keyboard.add(       InlineKeyboardButton('إستلام آية', callback_data='ayah'),
                        InlineKeyboardButton('إستلام حديث شريف', callback_data='sunah'))
    keyboard.add(       InlineKeyboardButton('للمساعدة', callback_data='help'))    
    return keyboard

