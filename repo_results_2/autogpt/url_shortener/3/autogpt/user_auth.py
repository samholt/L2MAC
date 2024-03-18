def register(username, password):
    users = read_file('users.json')
    if username in users:
        raise Exception('Username is already taken.')
    users[username] = {'password': password, 'urls': []}
    write_to_file('users.json', users)

def authenticate(username, password):
    users = read_file('users.json')
    if users.get(username, {}).get('password') == password:
        return True
    return False