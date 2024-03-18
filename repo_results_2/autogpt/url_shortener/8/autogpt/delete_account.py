import json

def delete_account(username):
    with open('users.json', 'r+') as file:
        data = json.load(file)
        if username in data:
            del data[username]
            file.seek(0)
            json.dump(data, file)
        else:
            return 'This username does not exist.'