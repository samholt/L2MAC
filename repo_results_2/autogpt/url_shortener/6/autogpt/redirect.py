import json

def redirect(short_url):
    with open('urls.json', 'r') as file:
        data = json.load(file)
        original_url = data.get(short_url)
        if original_url:
            return original_url
        else:
            return 'Error: Shortened URL does not exist.'