import json
from datetime import datetime


def update_analytics(short_url, location):
    with open('urls.json', 'r+') as f:
        data = json.load(f)
        for item in data:
            if item['short_url'] == short_url:
                if 'analytics' not in item:
                    item['analytics'] = []
                item['analytics'].append({'click_time': str(datetime.now()), 'location': location})
        f.seek(0)
        json.dump(data, f)

def get_analytics(short_url):
    with open('urls.json', 'r') as f:
        data = json.load(f)
        for item in data:
            if item['short_url'] == short_url:
                return item.get('analytics', [])
    return 'Short URL not found'