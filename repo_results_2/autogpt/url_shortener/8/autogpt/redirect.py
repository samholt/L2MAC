import json

def redirect(short_url):
    with open('urls.json', 'r') as file:
        data = json.load(file)
        original_url = data.get(short_url)
        return original_url