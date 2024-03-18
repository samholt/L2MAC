import json
import datetime

def set_expiration(username, url, expiration):
    with open('users.json', 'r+') as file:
        data = json.load(file)
        if username in data and url in data[username]['urls']:
            data[username]['urls'][url]['expiration'] = expiration
            file.seek(0)
            json.dump(data, file)
            return 'Expiration set successfully'
        else:
            return 'Invalid username or URL'

def check_expiration():
    with open('users.json', 'r+') as file:
        data = json.load(file)
        for username in data:
            for url in list(data[username]['urls']):
                if 'expiration' in data[username]['urls'][url] and datetime.datetime.now() > datetime.datetime.strptime(data[username]['urls'][url]['expiration'], '%Y-%m-%d %H:%M:%S'):
                    del data[username]['urls'][url]
        file.seek(0)
        json.dump(data, file)