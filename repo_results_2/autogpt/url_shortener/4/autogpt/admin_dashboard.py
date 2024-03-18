import json


def get_all_urls():
    with open('urls.json', 'r') as file:
        return json.load(file)


def delete_url(short_url):
    with open('urls.json', 'r+') as file:
        data = json.load(file)
        data = [item for item in data if item['short_url'] != short_url]
        file.seek(0)
        json.dump(data, file)


def get_all_users():
    with open('users.json', 'r') as file:
        return json.load(file)


def delete_user(username):
    with open('users.json', 'r+') as file:
        data = json.load(file)
        data = [item for item in data if item['username'] != username]
        file.seek(0)
        json.dump(data, file)