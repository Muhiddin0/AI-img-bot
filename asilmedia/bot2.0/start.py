from telegram.ext import (
    CallbackContext,
    )
from telegram import Update
import bot

""" START commandasi """
def start(update:Update, context:CallbackContext):

    username = update.message.from_user.first_name
    
    update.message.reply_html(\
f"""
🖖 Salom {username}

🟡 Men sizga hozircha kinolarni nomi orqali top beraman 
yangiliklarni kuzatib boring do'stim

🤖 version: 1.0
""")
    
    bot.selectLang(update, context)

  