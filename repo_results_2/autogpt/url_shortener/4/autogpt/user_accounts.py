import json


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.urls = []


def create_user(username, password):
    user = User(username, password)
    with open('users.json', 'r+') as file:
        data = json.load(file)
        data.append(user.__dict__)
        file.seek(0)
        json.dump(data, file)


def get_user(username):
    with open('users.json', 'r') as file:
        data = json.load(file)
        for item in data:
            if item['username'] == username:
                return User(**item)
    raise ValueError('User not found')