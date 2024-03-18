import json


def redirect(short_url):
    with open('urls.json', 'r') as f:
        data = json.load(f)
        for item in data:
            if item['short_url'] == short_url:
                return item['original_url']
    return 'Short URL not found'