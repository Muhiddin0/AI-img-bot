import requests
from bs4 import BeautifulSoup
import goslate


def imgSearching(update, context, imgUrl, user):
    url = f"https://yandex.uz/images/search?rpt=imageview&url={imgUrl}"

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

    text = ''
    c = 0

    title_box = soup.find(
        'section',
        {
            'class':'CbirSection CbirSection_decorated CbirTags'
        }
    )
    for item in title_box.find_all('a'):
        c += 1
        text += f'{c} <b>{item.text}</b> \n'

    update.message.reply_html(
f"""
💛 Natijalar

{text}

"""
)