import json


def view_all_urls():
    with open('urls.json', 'r') as f:
        data = json.load(f)
        return data

def delete_url(short_url):
    with open('urls.json', 'r+') as f:
        data = json.load(f)
        data = [item for item in data if item['short_url'] != short_url]
        f.seek(0)
        json.dump(data, f)
        return 'URL deleted'

def delete_user(username):
    with open('users.json', 'r+') as f:
        data = json.load(f)
        data = [item for item in data if item['username'] != username]
        f.seek(0)
        json.dump(data, f)
        return 'User deleted'