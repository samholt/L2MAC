import datetime

def set_expiration(short_url, expiration_date):
    with open('urls.json', 'r+') as file:
        urls = json.load(file)
        if short_url in urls:
            urls[short_url]['expiration'] = expiration_date
            json.dump(urls, file)
        else:
            return 'URL not found'
    return 'Expiration date set successfully'