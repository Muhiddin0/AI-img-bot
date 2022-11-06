from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def sendMedia(message, data, inline_btns):
    reply_markup = InlineKeyboardMarkup(row_width=10, inline_keyboard=inline_btns)

    await message.answer_photo(
        data['img'],
        caption=f"""<b>✔️ Nomi:</b> {data['nomi']}\n \n<b>🟢 Yili:</b> {data['yili']}\n \n<b>🔵 Davlati:</b> {data['davlati']}""",
        reply_markup = reply_markup,
        parse_mode='HTML',
    )

async def sendFilm(message, data):

    # game or movie test

    if data['content'] == "game":
        await message.answer("🔴 <b>Kechirasiz</b> ushbu content o'yin bolgani uchun uni sizga jo'nata olmadik", parse_mode='html')
        return
        
    inline_btns = []
    for i in range(int(len(data['data']))):
        
        inline_btns.append(
            [
                # InlineKeyboardButton(text=f"{data['data'][i]['title']}", callback_data=f"download_movie/{i}"),
                InlineKeyboardButton(text=f"✔️ yuklab olish", url=data['data'][i]['url'])
            ]
        )

        if len(inline_btns) == 20 or i == int(len(data['data'])) - 1:
            await sendMedia(message, data, inline_btns)
            inline_btns.clear()
