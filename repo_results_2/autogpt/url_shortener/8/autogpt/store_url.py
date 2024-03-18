import json
from datetime import datetime

def store_url(original_url, short_url, location, expiration=None):
    with open('urls.json', 'r+') as file:
        data = json.load(file)
        if short_url not in data:
            data[short_url] = {'original_url': original_url, 'clicks': 0, 'click_data': [], 'expiration': expiration}
        data[short_url]['clicks'] += 1
        data[short_url]['click_data'].append({'time': str(datetime.now()), 'location': location})
        file.seek(0)
        json.dump(data, file)