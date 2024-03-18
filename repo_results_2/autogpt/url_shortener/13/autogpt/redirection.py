import json

def redirect(short_url):
    with open('urls.json', 'r') as file:
        data = json.load(file)
        if short_url in data:
            return data[short_url]
        else:
            return 'Invalid short URL'