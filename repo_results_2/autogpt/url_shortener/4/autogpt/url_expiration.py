import json
from datetime import datetime


def set_expiration(short_url, expiration_datetime):
    with open('urls.json', 'r+') as file:
        data = json.load(file)
        for item in data:
            if item['short_url'] == short_url:
                item['expiration'] = expiration_datetime.isoformat()
        file.seek(0)
        json.dump(data, file)


def is_expired(short_url):
    with open('urls.json', 'r') as file:
        data = json.load(file)
        for item in data:
            if item['short_url'] == short_url:
                if 'expiration' in item and datetime.now() > datetime.fromisoformat(item['expiration']):
                    return True
        return False