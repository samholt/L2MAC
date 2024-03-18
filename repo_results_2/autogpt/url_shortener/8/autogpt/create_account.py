import json

def create_account(username, password):
    with open('users.json', 'r+') as file:
        data = json.load(file)
        if username in data:
            return 'This username is already in use.'
        else:
            data[username] = {'password': password, 'urls': []}
            file.seek(0)
            json.dump(data, file)