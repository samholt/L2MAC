import json
from datetime import datetime
import url_validation
import url_shortener


def shorten_url(url, expiration_date=None):
    if url_validation.validate_url(url):
        short_url = url_shortener.generate_short_url()
        with open('urls.json', 'r+') as f:
            data = json.load(f)
            data.append({'original_url': url, 'short_url': short_url, 'expiration_date': expiration_date})
            f.seek(0)
            json.dump(data, f)
        return short_url
    else:
        return 'Invalid URL'

def redirect(short_url):
    with open('urls.json', 'r') as f:
        data = json.load(f)
        for item in data:
            if item['short_url'] == short_url:
                if item['expiration_date'] and datetime.now() > datetime.strptime(item['expiration_date'], '%Y-%m-%d %H:%M:%S'):
                    return 'URL expired'
                return item['original_url']
    return 'Short URL not found'