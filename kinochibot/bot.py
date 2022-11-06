import requests
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentType
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.bot.api import TelegramAPIServer

from send_page import sendPageResult, editPageResult
from sendFilm import sendFilm
from update_film import updateFilm


# bot
# local_server = TelegramAPIServer.from_base('http://localhost:5000/')
API_TOKEN = "5691270645:AAGMsqZ4licqEcg_Tr_OoHE40cdzZtEdSFQ"
bot = Bot(API_TOKEN)
dp = Dispatcher(bot)


""" /start and /help commands"""
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("""🖖 Salom OP᭄ₘᵤₕᵢddᵢₙ꧂

🟡 Men sizga Filmalrni Nomi va Rasmi orqali topib beraman 
yangiliklarni kuzatib boring do'stim

🤖 version: 4.0""")
    await message.answer("""❗️ DIQQAT

Biz sizni harakatlaringizga javob bermaymiz
Iltimos botdna faqtat bo'sh vaqtingizda hordiq uchun foydalaning""")


""" Searching """
@dp.message_handler(content_types=ContentType.TEXT)
async def echo(message: types.Message):

    print('query =>', message.text)

    # data Json, API
    url = f"http://127.0.0.1:5000/{message.text}/1"
    data = requests.get(url).json()

    if bool(data['urls']):
        await sendPageResult(message, data, query=message.text)
    else:
        await message.answer("""🥺 Kechirasiz do'stim <b>Hechnarsa</b> topolmadim \n\n <i>So'rovingizni tekshirib qayta urinib ko'ring</i> 👉 /hatolar""", parse_mode='HTML')


""" Callback Data """
@dp.callback_query_handler()
async def callback_handler(callback: types.CallbackQuery):

    calData = callback.data
    key = calData.split('/')
    message = callback.message

    print('global', key)

    if key[0] == 'nexta_page': # pagelarni almashtirsh
        key = key[1].split('_')

        # data Json, API
        url = f"http://127.0.0.1:5000/{key[0]}/{key[1]}"
        print(url)
        data = requests.get(url).json()
        print(data)
        await editPageResult(message, data, key[0])
    elif key[0] == "select_film": #Kinoni tanlash

        data_urls_text_list = []
        for d in callback['message']['entities']:
            if d['type'] == 'text_link':
                data_urls_text_list.append(d['url'])

        selected_film_index = int(key[1])
        url_ = data_urls_text_list[selected_film_index].split('http://asilmedia.org/')

        print(url_)

        url = f"http://127.0.0.1:5000/downoad/{url_[1]}"
        data = requests.get(url).json()

        await sendFilm(message, data)
    elif key[0] == "download_movie": #kinoni yuklab olish
        await updateFilm(message, int(key[1]))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)