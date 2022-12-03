from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# my lib
from worker import working
from get_file_url import get_file_url

# translator API
import translators as tss


# Initialize bot and dispatcher
API_TOKEN = "5448993537:AAHV7lE8FCDWw2Bq_HwnOdMzEgz3km3p_jA"
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



# send welcome
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer(f"Salom <b>{message.from_user.first_name}</b>\n\nMen suniy AI orqali rasmlar blan Internet tarmog'idan <b>\nMalumotlar\nMaqolalar\nContentlar\nDublikat(siz jo'natganga o'xshash) rasmlarni \nTopib beraman \n\n Agar \"<b>Mohirfest</b>\"</b> loyihasi hakami bo'lsangiz /mohirfestbot ni bosing", parse_mode='html')
    await message.answer(f"<b>Ushbu AI voice blan boyiltilishini istasangiz \"@muhiddinKabiraliev\"ga murojat qiling</b>", parse_mode='html')

# send info bot
@dp.message_handler(commands=['mohirfestbot'])
async def send_info_bot(message: types.Message):

    await message.answer('salom')
    await message.answer_video(
        "https://t.me/kmTestFest/2",
        caption=\
"""
<b>
Aloqa uchun

+998905650213
@muhiddinKabiraliev
</b>
""", parse_mode='HTML',
        )


@dp.message_handler(content_types='photo')
async def workingAI(message: types.Message):

    msg = await message.answer("<b>🔎 Qidirilmoqda \n\n Bu biroz vaqt talab qiladi</b>", parse_mode='html')
    
    # install data
    img_url = await get_file_url(message.photo[2].file_id)
    dataJson = await working(img_url)

    # fixeding BUG
    if dataJson['problem'] == True:
        await msg.edit_text("<b>😞 Kechirasiz sizning so'rov bo'yicha tarmoqda hechqanday ma'lumot mavjud emas</b>", parse_mode='html')
        return
    
    # SENDING Message
    # tss.translate_text(chs_text, from_language='auto', to_language='uz')
    for card_data in dataJson['data'][0:15]:
        try:
            title_text = tss.translate_text(card_data['title'], from_language='auto', to_language='uz')
            description_text = tss.translate_text(card_data['description'], from_language='auto', to_language='uz')
            await message.answer_photo(
                photo=card_data['originalImage']['url'],
                caption=f"""
<b>{title_text}</b>

<i>{description_text}</i>

<b>Manzil:</b> {card_data['domain']}
""", reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton('🕸 Maqola 🕸', url=f"""{card_data['url']}""")]]),
                parse_mode="html"
            )
        except:
            pass


    # umumiy malumot
    short_result_caption = ''
    for result in dataJson['tags']:
        short_result_caption += "\n<b>🟡 " + tss.translate_text(result['text'], from_language='auto', to_language='uz') + "</b> \n"

    await message.answer_photo(
        photo=message.photo[2].file_id,
        caption=\
f"""
Sizning so'rov bo'yich malumotlar

{short_result_caption}
""",    parse_mode='HTML'
    )

@dp.message_handler(content_types=types.ContentTypes.ANY)
async def workingAI(message: types.Message):
    await message.answer("""<b>🔴 Iltimos menga to'g'ri malumot kiriting</b>""", parse_mode='html')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)