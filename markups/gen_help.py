from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def gen_help():
    keyboard = InlineKeyboardMarkup()
    keyboard.row_width = 2
    keyboard.add(       InlineKeyboardButton('التواصل مع المطوّر', url='telegram.me/mal_0'),
                        InlineKeyboardButton('البداية', callback_data='start'))
    keyboard.add(       InlineKeyboardButton('إستلام آية', callback_data='ayah'),
                        InlineKeyboardButton('إستلام حديث شريف', callback_data='sunah'))

    keyboard.add(       InlineKeyboardButton('السابق  <<', callback_data='start'))
    return keyboard

