import json
import datetime
import geocoder

def record_click(short_url):
    with open('urls.json', 'r+') as file:
        data = json.load(file)
        if short_url in data:
            if 'clicks' not in data[short_url]:
                data[short_url]['clicks'] = []
            click_data = {
                'time': str(datetime.datetime.now()),
                'location': geocoder.ip('me').latlng
            }
            data[short_url]['clicks'].append(click_data)
            file.seek(0)
            json.dump(data, file)
        else:
            return 'Invalid short URL'