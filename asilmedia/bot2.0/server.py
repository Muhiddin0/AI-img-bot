
""" IMPORT ALL MODULS """
from telegram.ext import (
    CallbackContext
    )
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup


# tilni tanlash functsiyasi
def selectServer(update:Update, context:CallbackContext):
    inlineBtns = [
        [
            InlineKeyboardButton('asilmedia', callback_data='asilmedia'),
        ]
    ]
    update.message.reply_text(
"""
💁 Filmlarni qayerdan topmoqchisiz

✅ Hozirda foydalanilyotgan server = asilmedi
""",
    reply_markup=InlineKeyboardMarkup(inlineBtns)
    )
