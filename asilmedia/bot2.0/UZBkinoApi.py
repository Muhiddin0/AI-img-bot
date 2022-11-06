


"""
================
   KUTUBXONA 
"""
from bs4 import BeautifulSoup
import requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
"""
================
"""



"""
=================
"""
def kinoQidirish(url):

        """====> sayitni olish <===="""
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')

        """ ===> kino kardlarini olish<==== """
        cardlar = soup.find_all('article', {'class':'shortstory-item moviebox to-ripple is-green anima'})

        """ ===>linolarni json formati<=== """
        kinoLinklari = []


        "====>kardgadan malumot olish<===="
        for kard in cardlar:
            
            kino = {
                'link':'',
                'title':''
            }
            kard = BeautifulSoup(str(kard), 'lxml')

            """ html-linkga borish """
            html_link = kard.find(
                'a',
                {
                    'class':'flx flx-column flx-column-reverse',
                    'href':True,
                    }
                )
            link = html_link['href']
            kino['link'] = link

            """ titlega borish """
            title = kard.find(
                'h2',
                {
                    'class':'title is-6 txt-ellipsis mb-2'
                }
            )
            kino['title'] = title.text
            kinoLinklari.append(kino)
            
        return kinoLinklari
"""
=================
"""




"""
===================================================
            || Pagelarni aniqlash ||
===================================================
"""
def UZBkinoApi(query):

    data = []

    """====> sayitni olish <===="""
    url = f"http://asilmedia.org/index.php?story={query}&search_start=1&do=search&subaction=search"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

    """ Pagelarni aniqlash """
    page_box = soup.find(
        'div',
            {
                'class':'navigation fx-row fx-start'
            }
        )
    
    if bool(page_box):
        
        page_count = page_box.find_all('a')[-1].text
        page_count = int(page_count) + 1
        print(page_count)

        for item in range(1, page_count):
            data.append(kinoQidirish(f"http://asilmedia.org/index.php?story={query}&search_start={item}&do=search&subaction=search"))
    else:
        data.append(kinoQidirish(f"http://asilmedia.org/index.php?story={query}&search_start=1&do=search&subaction=search"))
    
    
    return data
"""




===================================================
          || KINO OLISH JSON ||
===================================================
"""
def kinoOlish(query, url, seconary):
      
    dataJson = {
        "film-title":"",
        "film-img": "",
        "film-sanasi":"",
        "film-likelari":{
                'like': '',
                'dez-like': ''
            },
        "film-haqida":"",
        "film-janri":"",
        "film-download":[]
    }

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

    try:
        """ title """
        title = soup.find(
            'h1',
            {
                'class':'title is-4 mb-2'
            }
        )
        dataJson['film-title'] = title.text
    except:
        dataJson['film-title'] = 'Noaniq'

    try:        
        """ film img """
        film_img = soup.find_all(
            'picture',
            {
                'class':'poster-img poster-imgresp is-5'
            }
        )[0]
        film_img = BeautifulSoup(str(film_img), 'lxml').find(
            'img',
            {
                'data-src':True
            }
            )
        dataJson['film-img'] = f"http://asilmedia.org{film_img['data-src']}"
    except:
        dataJson['film-img'] = "http://asilmedia.org/templates/playfilmo/dleimages/no_image.jpg"
        
    try:
        """film-sanasi"""
        film_sanasi = soup.find(
            'div',
            {
                'class':'full-head-col flx flx-column'
            }
            )
        dataJson["film-sanasi"] = film_sanasi.find('time')['datetime']
    except:
        dataJson["film-sanasi"] = 'Noaniq'

    try:
        """film-likelari"""
        film_likes_box = soup.find(
            'div',
            {
                'class':'frate-ud flx align-items-center justify-content-end mb-2'
            }
        )
        film_like = film_likes_box.find(
            'span',
            {
                'class':'ignore-select'
            }
            )
        film_dez_like = film_likes_box.find_all(
        'span',
        {
            'class':'ignore-select'
        }
        )
    
        dataJson["film-likelari"]['like'] = film_like.text
        dataJson["film-likelari"]['dez-like'] = film_dez_like[1].text
    except:
        dataJson["film-likelari"]['like'] = 'Noaniq'
        dataJson["film-likelari"]['dez-like'] = 'Noaniq'

    
    try:
        """"film-janri"""
        film_janri = soup.find_all(
            'div',
            {
                'class':'fullinfo-list mb-2'
            }
        )[0]
        film_janri = BeautifulSoup(str(film_janri), 'lxml').find_all('span')[1].text
        dataJson['film-janri'] = film_janri

    except:
        dataJson['film-janri'] = 'Noaniq'


    try:
        """ filmhaqida qisqacha """
        film_haqida = soup.find(
            'p',
            {'class':'full-text full-storyimg mb-3'}
            )
        dataJson['film-haqida'] = film_haqida.text
    except:
        dataJson['film-haqida'] = 'Noaniq'


    """film-download"""
    btn_box = soup.find(
        'div',
        {
            'class':'downlist-inner flx flx-column'
        }
    )
    btns = btn_box.find_all(
        'a',
        {
            'href':True,
            'download':True
        }
        )

    for btn in btns:

        film_down_link = {
            'download-link':"",
            'download-title':''
        }
        
        
        if btn['href'] != 'https://t.me/+gE5tqpLjhiNlNWIy': # telegram canal linkini chiqarib tashlash
            
            # urlni budagn saqlash
            cut = btn['href'].split('http://')
            download_url = 'http://'+cut[1]

            # tayyor urlni va titleni bazaga joylash
            film_down_link['download-link'] = download_url
            film_down_link['download-title'] = btn.text
            
            # kinoni bazaga kiritish
            dataJson['film-download'].append(film_down_link)
    
    
    if dataJson['film-download'] == []:

        ifram = soup.find(
            'div',
            {
                'id':'onlayn1'
            }
        )

        video = ifram.find_all('iframe',{"src":True})
        title = soup.find('h1',{'class':"title is-4 mb-2"})


        if video != []:
            film_down_link = {
                'download-link':"",
                'download-title':f'{title.text}'
            }
            for item in video:
                film_down_link['download-link'] = item['src']
                dataJson['film-download'].append(film_down_link )
        else:
            query.message.reply_html('💁 <b>Kechirasiz</b> ushbu content \nAdminlar tomonidan yo\'q qilingan')
                        

    """
        <====== Update content user ========>
    """
    cap = \
f"""
✅ Nomi: {dataJson['film-title']}

📅 Sansi: {dataJson['film-sanasi']}


❤️ Like: {dataJson['film-likelari']['like']}, {dataJson['film-likelari']['dez-like']}

🌴 Janri: {dataJson['film-janri']}

👨‍💻 Admin: @proCoder2005
🤖 Bot: @KinochiUzbBot

"""
    
    for down in dataJson['film-download']:
        try:
            # seconary.message.delete()
            query.message.reply_photo(
                dataJson['film-img'],
                caption=cap,
                parse_mode='html',
                reply_markup=InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton(f"{down['download-title']}", callback_data='click 1', url=down['download-link'])]
                        ]
                    )
            )
        except:
            pass
