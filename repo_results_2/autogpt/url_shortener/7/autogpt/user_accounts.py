def create_account(username, password):
    with open('users.json', 'r+') as file:
        users = json.load(file)
        if username in users:
            return 'Username already exists'
        users[username] = {'password': password, 'urls': []}
        json.dump(users, file)
    return 'Account created successfully'