import json


def redirect(short_url):
    with open('urls.json', 'r') as file:
        data = json.load(file)
        for item in data:
            if item['short_url'] == short_url:
                return item['original_url']
    raise ValueError('Short URL not found')