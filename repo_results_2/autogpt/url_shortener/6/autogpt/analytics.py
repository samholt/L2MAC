import json
from datetime import datetime

def track_click(short_url):
    with open('urls.json', 'r+') as file:
        data = json.load(file)
        if short_url in data:
            if 'clicks' in data[short_url]:
                data[short_url]['clicks'].append(str(datetime.now()))
            else:
                data[short_url]['clicks'] = [str(datetime.now())]
            file.seek(0)
            json.dump(data, file)
        else:
            return 'Error: Shortened URL does not exist.'

def get_clicks(short_url):
    with open('urls.json', 'r') as file:
        data = json.load(file)
        if short_url in data and 'clicks' in data[short_url]:
            return data[short_url]['clicks']
        else:
            return 'Error: No clicks data available.'