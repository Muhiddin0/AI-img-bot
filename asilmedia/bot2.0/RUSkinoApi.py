
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

kinoQidirish('https://tas-ix.media/films/i/14296-shelbilar-oilasi-6-sezon-4-chasti-iz-6-ostrye-kozyrki-zatochennye-kepki-uzbek-tilida-ozbekcha-tarjima-barcha-qismlari.html')