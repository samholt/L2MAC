import json

def store_urls(original_url, short_url):
    with open('urls.json', 'r+') as file:
        data = json.load(file)
        data[short_url] = original_url
        file.seek(0)
        json.dump(data, file)