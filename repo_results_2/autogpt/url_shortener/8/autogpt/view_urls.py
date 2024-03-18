import json

def view_urls(username):
    with open('users.json', 'r') as file:
        data = json.load(file)
        if username in data:
            return data[username]['urls']
        else:
            return 'This username does not exist.'