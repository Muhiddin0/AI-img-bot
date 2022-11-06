from aiogram import types


async def updateFilm(message: types.Message, select):

    data = message['reply_markup']['inline_keyboard'][select][1]['url']
    print(data)
    
    await message.answer_video(data)
