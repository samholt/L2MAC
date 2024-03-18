def create_account(username, password):
    # Read the users file
    with open('users.json', 'r') as file:
        users = json.load(file)
    # Check if the username is already taken
    for user in users:
        if user['username'] == username:
            return 'Error: Username already taken'
    # If the username is not taken, create a new account
    new_user = {'username': username, 'password': password, 'urls': []}
    users.append(new_user)
    # Write the updated users data back to the file
    with open('users.json', 'w') as file:
        json.dump(users, file)
    return 'Account created successfully'