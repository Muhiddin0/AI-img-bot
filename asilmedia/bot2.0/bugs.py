
""" IMPORT ALL MODULS """
from telegram.ext import (
        CallbackContext,
    )
from telegram import Update

def problemCommand(update:Update, context:CallbackContext):
    update.message.reply_text('⚠️ Not\'g\'ri commanda')

def notCommand(update:Update, context:CallbackContext):
    update.message.reply_text('😄 Ushbu bo\'lim tez kunda ishga tushadi INSHA ALLAH')
