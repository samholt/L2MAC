import json
from datetime import datetime

def set_expiration(url, expiration_date):
    with open('urls.json', 'r+') as file:
        urls = json.load(file)
        if url in urls:
            urls[url]['expiration_date'] = expiration_date
            file.seek(0)
            json.dump(urls, file)
            return 'Expiration date set successfully.'
        else:
            return 'Error: URL does not exist.'

def check_expiration(url):
    with open('urls.json', 'r+') as file:
        urls = json.load(file)
        if url in urls and 'expiration_date' in urls[url] and datetime.now() > datetime.strptime(urls[url]['expiration_date'], '%Y-%m-%d %H:%M:%S'):
            del urls[url]
            file.seek(0)
            json.dump(urls, file)
            return 'URL expired and deleted.'
        else:
            return 'URL is not expired.'