import json


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.urls = []


def create_user(username, password):
    user = User(username, password)
    with open('users.json', 'r+') as f:
        data = json.load(f)
        data.append(user.__dict__)
        f.seek(0)
        json.dump(data, f)

def get_user_urls(username):
    with open('users.json', 'r') as f:
        data = json.load(f)
        for item in data:
            if item['username'] == username:
                return item['urls']
    return 'User not found'

def edit_user_url(username, old_url, new_url):
    with open('users.json', 'r+') as f:
        data = json.load(f)
        for item in data:
            if item['username'] == username:
                if old_url in item['urls']:
                    item['urls'].remove(old_url)
                    item['urls'].append(new_url)
                    f.seek(0)
                    json.dump(data, f)
                    return 'URL updated'
                else:
                    return 'URL not found'
    return 'User not found'

def delete_user_url(username, url):
    with open('users.json', 'r+') as f:
        data = json.load(f)
        for item in data:
            if item['username'] == username:
                if url in item['urls']:
                    item['urls'].remove(url)
                    f.seek(0)
                    json.dump(data, f)
                    return 'URL deleted'
                else:
                    return 'URL not found'
    return 'User not found'