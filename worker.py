import requests
from bs4 import BeautifulSoup
import json

async def working(img_url):

    # install web-site
    url = f"https://yandex.uz/images/search?rpt=imageview&url={img_url}"
    r = requests.get(url)

    # main Soup
    soup = BeautifulSoup(r.text, "lxml")
    boxs = soup.find_all('div', {
        "class":"Root",
        "data-hydrate-priority":True,
        "data-state":True
        }
    )

    tags = json.loads(boxs[3]["data-state"])
    data = json.loads(boxs[2]['data-state'])
    
    try:    
        return {"data":data['sites'], "tags":tags['tags'], "problem":False}
    except:
        return {"data":False, "tags":False, "problem":True}
    
# working(
#     "https://docs.aiogram.dev/en/latest/_static/logo.png"
# )