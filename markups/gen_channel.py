from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
def gen_channel():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(       InlineKeyboardButton('إستلام آية', callback_data='ayah'),
                        InlineKeyboardButton('إستلام حديث شريف', callback_data='sunah'))

    markup.add(                 InlineKeyboardButton("السابق  <<", callback_data="back"))
    return markup
