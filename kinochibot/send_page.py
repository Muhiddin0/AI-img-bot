from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests


async def sendPageResult(message, data, query):

    # Message vars  
    c = 0
    cap = f"""{data['now-page']}/{data['max-pages']}\n"""
    inline_btns = [
        [],[]
    ]
    
    for d in data['urls']:
        c += 1
        cap += f"<b>{c}) {d['name']}</b> \n 🟡 <a href='{d['url']}'> Online Ko'rish </a> \n\n"
        if len(inline_btns[0]) >= 5:
            inline_btns[1].append(   
                InlineKeyboardButton(text=f"{c}", callback_data=f"select_film/{c - 1}")
            )
        else:
            inline_btns[0].append(   
                InlineKeyboardButton(text=f"{c}", callback_data=f"select_film/{c - 1}")
            )
    
    control_btns = []
    if data['max-pages'] == "yakka-page":
        pass
    elif data['now-page'] == "1":
        control_btns.append(
            InlineKeyboardButton(text=f"Oldinga ➡️", callback_data=f"nexta_page/{query}_{int(data['now-page']) + 1}")
        )
    elif data['max-pages'] == data['now-page']:
        control_btns.append(
            InlineKeyboardButton(text=f"⬅️ Orqaga", callback_data=f"nexta_page/{query}_{int(data['now-page']) - 1}")
        )
    else:
        control_btns.append(
            InlineKeyboardButton(text=f"⬅️ Orqaga", callback_data=f"nexta_page/{query}_{int(data['now-page']) - 1}"),
            InlineKeyboardButton(text=f"Oldinga ➡️", callback_data=f"nexta_page/{query}_{int(data['now-page']) + 1}")
        )
    inline_btns.append(control_btns)

    reply_markup = InlineKeyboardMarkup(row_width=5, inline_keyboard=inline_btns)

    await message.answer(cap, parse_mode='html', reply_markup=reply_markup)


async def editPageResult(message, data, query):

    # Message vars  
    c = 0
    cap = f"""{data['now-page']}/{data['max-pages']}\n"""
    inline_btns = [
        [],[]
    ]
    
    for d in data['urls']:
        c += 1

        cap += f"<b>{c}) {d['name']}</b> \n 🟡 <a href='{d['url']}'> Online Ko'rish </a> \n\n"

        if len(inline_btns[0]) >= 5:
            inline_btns[1].append(
                InlineKeyboardButton(text=f"{c}", callback_data=f"select_film/{c - 1}")
            )
        else:
            inline_btns[0].append(   
                InlineKeyboardButton(text=f"{c}", callback_data=f"select_film/{c - 1}")
            )
    
    control_btns = []
    if data['max-pages'] == "yakka-page":
        pass
    elif data['now-page'] == "1":
        control_btns.append(
            InlineKeyboardButton(text=f"Oldinga ➡️", callback_data=f"nexta_page/{query}_{int(data['now-page']) + 1}")
        )
    elif data['max-pages'] == data['now-page']:
        control_btns.append(
            InlineKeyboardButton(text=f"⬅️ Orqaga", callback_data=f"nexta_page/{query}_{int(data['now-page']) - 1}")
        )
    else:
        control_btns = [
            InlineKeyboardButton(text=f"⬅️ Orqaga", callback_data=f"nexta_page/{query}_{int(data['now-page']) - 1}"),
            InlineKeyboardButton(text=f"Oldinga ➡️", callback_data=f"nexta_page/{query}_{int(data['now-page']) + 1}")
        ]
    inline_btns.append(control_btns)

    reply_markup = InlineKeyboardMarkup(row_width=5, inline_keyboard=inline_btns)

    await message.edit_text(cap, parse_mode='html', reply_markup=reply_markup)
