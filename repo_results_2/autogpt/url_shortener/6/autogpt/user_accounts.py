import json

def get_urls(username):
    with open('users.json', 'r') as file:
        users = json.load(file)
        if username in users:
            return users[username]['urls']
        else:
            return 'Error: User does not exist.'

def edit_url(username, old_url, new_url):
    with open('users.json', 'r+') as file:
        users = json.load(file)
        if username in users and old_url in users[username]['urls']:
            users[username]['urls'][new_url] = users[username]['urls'].pop(old_url)
            file.seek(0)
            json.dump(users, file)
            return 'URL edited successfully.'
        else:
            return 'Error: User or URL does not exist.'

def delete_url(username, url):
    with open('users.json', 'r+') as file:
        users = json.load(file)
        if username in users and url in users[username]['urls']:
            del users[username]['urls'][url]
            file.seek(0)
            json.dump(users, file)
            return 'URL deleted successfully.'
        else:
            return 'Error: User or URL does not exist.'