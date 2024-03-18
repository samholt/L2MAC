import json

def view_all_urls():
    with open('urls.json', 'r') as file:
        data = json.load(file)
        return data