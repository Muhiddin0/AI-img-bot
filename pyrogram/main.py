import asyncio
from pyrogram import Client

api_id = 18349141
api_hash = "fa3a10f79ac5765fa9cd9a977a1923d3"


async def main():
    async with Client("my_account", api_id, api_hash) as app:
        await app.send_message("me", "Greetings from **Pyrogram**!")
        await app.send_video("me", "http://fayllar1.ru/25/Seriallar/Ayol%20Halk/Ayol%20Halk%20f01q01%20AQSH%20seriali%20O'zbek%20tilida%20(asilmedia.net).m4v")

asyncio.run(main())