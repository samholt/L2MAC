import datetime
import geocoder

def record_click(short_url):
    g = geocoder.ip('me')
    location = g.latlng
    time = datetime.datetime.now()
    with open('analytics.txt', 'a') as file:
        file.write(f'{short_url} {time} {location}\n')