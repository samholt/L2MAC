import json

def delete_url(username, short_url):
    with open('users.json', 'r+') as file:
        data = json.load(file)
        if username in data:
            if short_url in data[username]['urls']:
                data[username]['urls'].remove(short_url)
                file.seek(0)
                json.dump(data, file)
            else:
                return 'This short URL does not exist.'
        else:
            return 'This username does not exist.'