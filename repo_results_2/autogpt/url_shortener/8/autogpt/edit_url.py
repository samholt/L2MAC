import json

def edit_url(username, old_short_url, new_short_url):
    with open('users.json', 'r+') as file:
        data = json.load(file)
        if username in data:
            if old_short_url in data[username]['urls']:
                data[username]['urls'].remove(old_short_url)
                data[username]['urls'].append(new_short_url)
                file.seek(0)
                json.dump(data, file)
            else:
                return 'This short URL does not exist.'
        else:
            return 'This username does not exist.'