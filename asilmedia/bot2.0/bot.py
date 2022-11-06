
""" IMPORT ALL MODULS """
import UZBkinoApi
import img
from telegram.ext import (
    Updater,
    CallbackContext,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler,
    )
from telegram import Update, File ,ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from bugs import *
from server import selectServer

"<=== bot statelari va asosiy tugmalr ===>"
# statelar
RUNBOT, KINO_QIDIRISH_TANLOVI, NOMI_BLAN_QIDIRISH, IMG_BLAN_QIDIRIDH, FILTERLASH = range(5)

# <== TUGMALAR ===>
asosiyMenuBTN = ReplyKeyboardMarkup([
    ['🔍 Qidirish', '🗂 Filterlash'],
    ['🎲 Tasodifiy']
], resize_keyboard=True)

filmQidirishMenuBTN = ReplyKeyboardMarkup([
        ['🖼 Rasmi', '📝 Nomi'],
        ['🔙 Back']
], resize_keyboard=True)
filterBtns = ReplyKeyboardMarkup([
    ["Ko'p ko'rilgan", "So'ngi qo'shilgan"],
    ["Filmlar", "seriallar"],
    ["Multifilmlar","Klip"],
    ['🔙 Back']
], resize_keyboard=True)
backBtn =ReplyKeyboardMarkup([
    ['🔙 Back']
], resize_keyboard=True)





"<== yordamchi functsiyalar ===>"
def mainMenu(update:Update, context:CallbackContext):
    update.message.reply_html('✅ Asosiy menu', reply_markup=asosiyMenuBTN)
    return ConversationHandler.END



"<=== asosiy functsiyalar ===>"

# START commandasi
def start(update:Update, context:CallbackContext):

    username = update.message.from_user.first_name
    
    update.message.reply_html(\
f"""
🖖 Salom {username}

🟡 Men sizga hozircha kinolarni nomi orqali top beraman 
yangiliklarni kuzatib boring do'stim

🤖 version: 1.0
""", reply_markup=asosiyMenuBTN)
    
    selectServer(update, context)

    return ConversationHandler.END



    
"""<=== user data ===>"""
user = {
    'server':'asilmedia'
}
def callback_btn(update:Update, context:CallbackContext):

    query = update.callback_query
    callback_data_q = query.data

    if callback_data_q == 'asilmedia' or callback_data_q == 'rus' or callback_data_q == 'eng':
        user['lang'] = callback_data_q
        query.message.delete()
        
        query.message.reply_html(
            f"""👌 Marhamat endi siz \nkinolarni <i>{callback_data_q}</i>"dan \ntopishingiz mumkin"""
            )

    try:
        i = int(callback_data_q)
    except:
        pass
    else:

        urls = []
        for item in query.message.entities:
            if item['url'] != None:
                urls.append(item['url'])
        
        i = int(i)
        index = urls[i]
        seconary = query.message.reply_text('🆗 Film jo\'natilmoqda')

        UZBkinoApi.kinoOlish(query, index, seconary)


"""<=== state KinoQidiruv ===>"""
def stateKinoQidiruv(update:Update, context:CallbackContext):
    update.message.reply_text(
        "🎞 Filmni qaysi yo'l blan topmoqchisiz",
        reply_markup=filmQidirishMenuBTN
        )
    return KINO_QIDIRISH_TANLOVI

def nomiBlanQidirish(update:Update, context:CallbackContext):
    update.message.reply_text(
        '🆗 Marhamat menga kino nomini kiriting',
        reply_markup=backBtn
        )
    return NOMI_BLAN_QIDIRISH

def kinoQidirish(update:Update, context:CallbackContext):

    msg1 = update.message.reply_text(
        'iltimos biroz kuting'
        )
    msg2 = update.message.reply_sticker('CAACAgIAAxkBAAEBXG1jPSHY6CawIc3OLmLGSIEciH6A7QAClgoAAmXXSEqeC5Vjb_xP4CoE')

    if user['server'] =='asilmedia':
        data = UZBkinoApi.UZBkinoApi(update.message.text)
    elif user['lang'] == 'rus':
        pass
    elif user['lang'] == 'eng':
        pass

    if bool(data[0]):
        
        for page in data:
            btn = [
                []
            ]
            msg = ''
            c = 0

            for card in page:
                c += 1
                
                if c == 6:
                    btn.append([])
                    
                if len(btn) == 2:
                    btn[1].append(
                        InlineKeyboardButton(f'{c}', callback_data=f'{c - 1}')
                    )
                else:
                    btn[0].append(
                        InlineKeyboardButton(f'{c}', callback_data=f'{c - 1}')
                    )

                msg += f'''\n <b>{c}</b> ✅ Nomi: {card['title']} \n manzili: <a href="{card['link']}">website</a>'''

            update.message.reply_html(msg, reply_markup=InlineKeyboardMarkup(btn))
    
    else:
        update.message.reply_text('🥺 Kechirasiz bunday content topilmadi')
    
    context.bot.deleteMessage(message_id = msg1.message_id, chat_id = update.message.chat_id)
    context.bot.deleteMessage(message_id = msg2.message_id, chat_id = update.message.chat_id)

""" rasm orqali kino qidiruv """
def serchingPhotoState(update:Update, context:CallbackContext):

    update.message.reply_html(
        "🖼 Rasm blan qulay qidirish \n\n⚠️ Rasm orqali to'g'ri qidirishni /help orqali o'rganing",
        reply_markup=backBtn
        )
    return IMG_BLAN_QIDIRIDH

def searchingPhoto(update:Update, context:CallbackContext):
    
    file = update.message.photo[0].file_id
    obj = context.bot.get_file(file)
    urlImg = obj.file_path

    img.imgSearching(update, context, urlImg, user)


"""<=== FILER ====>"""
def stateFilterlash(update:Update, context:CallbackContext):
    update.message.reply_html("""🙂 Filterlash orqali kerakli kinoni toping""", reply_markup=filterBtns)
    return FILTERLASH



"""<=== state Filterlash ===>"""
    
    
def main():

    """ bot """
    updater = Updater('5798866586:AAEp4bTyLha0NETMqV-AUDeKpGl5R_PwTcE', use_context=True)
    dispatcher = updater.dispatcher
     
    
    """ commands """
    conv_qidirish = ConversationHandler(
        entry_points = [
            MessageHandler(Filters.regex('^(🔍 Qidirish)$'), stateKinoQidiruv),                
            MessageHandler(Filters.regex('^(🗂 Filterlash)$'), notCommand),
            MessageHandler(Filters.regex('^(🎲 Tasodifiy)$'), notCommand)
        ],
        states={
            
            KINO_QIDIRISH_TANLOVI:[
                MessageHandler(Filters.regex('^(🔙 Back)$'), mainMenu),
                MessageHandler(Filters.regex('^(📝 Nomi)$'), nomiBlanQidirish),
                MessageHandler(Filters.regex('^(🖼 Rasmi)$'), serchingPhotoState),
                MessageHandler(Filters.regex('^(🎞 Shot video)$'), notCommand),
            ],      
            NOMI_BLAN_QIDIRISH:[
                MessageHandler(Filters.regex('^(🔙 Back)$'), stateKinoQidiruv),
                MessageHandler(Filters.text, kinoQidirish),
            ],
            IMG_BLAN_QIDIRIDH:[
                MessageHandler(Filters.regex('^(🔙 Back)$'), stateKinoQidiruv),
                MessageHandler(Filters.photo, searchingPhoto),
            ],
            
            FILTERLASH:[
                MessageHandler(Filters.regex('''^(Ko'p ko'rilgan)$'''), notCommand),
                MessageHandler(Filters.regex('''^(So'ngi qo'shilgan)$'''), notCommand),
                MessageHandler(Filters.regex('''^(Filmlar)$'''), notCommand),
                MessageHandler(Filters.regex('''^(seriallar)$'''), notCommand),
                MessageHandler(Filters.regex('''^(Multifilmlar)$'''), notCommand),
                MessageHandler(Filters.regex('''^(Klip)$'''), notCommand),
                MessageHandler(Filters.regex('^(🔙 Back)$'), mainMenu),
            ]
        },
        fallbacks=[
            MessageHandler(Filters.all, problemCommand)
        ]
    )
    
    
    dispatcher.add_handler(CommandHandler('start', start)),
    dispatcher.add_handler(CommandHandler('server', selectServer)),
    dispatcher.add_handler(conv_qidirish),
    dispatcher.add_handler(CallbackQueryHandler(callback_btn)),
    dispatcher.add_handler(MessageHandler(Filters.all, problemCommand))


    
    
    """ run """
    updater.start_polling()
    updater.idle()
main()