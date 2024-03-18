import json
from datetime import datetime


def update_click_data(short_url, location):
    with open('urls.json', 'r+') as file:
        data = json.load(file)
        for item in data:
            if item['short_url'] == short_url:
                if 'click_data' not in item:
                    item['click_data'] = []
                item['click_data'].append({'timestamp': datetime.now().isoformat(), 'location': location})
        file.seek(0)
        json.dump(data, file)


def get_click_data(short_url):
    with open('urls.json', 'r') as file:
        data = json.load(file)
        for item in data:
            if item['short_url'] == short_url:
                return item.get('click_data', [])
    raise ValueError('Short URL not found')