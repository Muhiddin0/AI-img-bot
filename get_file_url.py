import requests
bot_token = "5448993537:AAHV7lE8FCDWw2Bq_HwnOdMzEgz3km3p_jA"

async def get_file_url(file_id):

    get_file_id = f"https://api.telegram.org/bot{bot_token}/getFile?file_id={file_id}"
    r = requests.get(get_file_id).json()
    
    return f"https://api.telegram.org/file/bot{bot_token}/{r['result']['file_path']}"