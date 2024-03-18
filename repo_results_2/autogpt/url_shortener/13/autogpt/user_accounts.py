import json

def create_account(username, password):
    with open('users.json', 'r+') as file:
        data = json.load(file)
        if username in data:
            return 'Username already exists'
        else:
            data[username] = {
                'password': password,
                'urls': {}
            }
            file.seek(0)
            json.dump(data, file)
            return 'Account created successfully'

def view_urls(username):
    with open('users.json', 'r') as file:
        data = json.load(file)
        if username in data:
            return data[username]['urls']
        else:
            return 'Invalid username'

def edit_url(username, old_url, new_url):
    with open('users.json', 'r+') as file:
        data = json.load(file)
        if username in data and old_url in data[username]['urls']:
            data[username]['urls'][new_url] = data[username]['urls'].pop(old_url)
            file.seek(0)
            json.dump(data, file)
            return 'URL edited successfully'
        else:
            return 'Invalid username or URL'

def delete_url(username, url):
    with open('users.json', 'r+') as file:
        data = json.load(file)
        if username in data and url in data[username]['urls']:
            del data[username]['urls'][url]
            file.seek(0)
            json.dump(data, file)
            return 'URL deleted successfully'
        else:
            return 'Invalid username or URL'

def view_analytics(username, url):
    with open('users.json', 'r') as file:
        data = json.load(file)
        if username in data and url in data[username]['urls']:
            return data[username]['urls'][url]['clicks']
        else:
            return 'Invalid username or URL'